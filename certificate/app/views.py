
from django.shortcuts import get_object_or_404, render, redirect
# from django.http import HttpResponse
from .models import Employee, Skill

def add_employee_and_skills(request):
    if request.method == 'POST':
        # Extract data from POST request
        image = request.FILES.get('image')
        c_image = request.FILES.get('c_image')
        name = request.POST.get('name')
        certificate_id = request.POST.get('certificate_id')
        department_name = request.POST.get('department_name')
        position = request.POST.get('position')
        joining_date = request.POST.get('joining_date')
        leaving_date = request.POST.get('leaving_date')
        worked_in = request.POST.get('worked_in')
        tl_review = request.POST.get('tl_review')
        dh_review = request.POST.get('dh_review')
        feedback = request.POST.get('feedback')
        

        # Create Employee instance
        employee = Employee(
            name=name, certificate_id=certificate_id, department_name=department_name,position=position,
            joining_date=joining_date, leaving_date=leaving_date, worked_in=worked_in,
            tl_review=tl_review, dh_review=dh_review, feedback=feedback, image=image,certificate=c_image
        )
        employee.save()

        skills = request.POST.getlist('skills')
        ratings = request.POST.getlist('ratings')
        for skill, rating in zip(skills, ratings):
            if skill:  # Making sure a skill name was actually provided
                Skill.objects.create(employee=employee, skill=skill, rating=int(rating))

        return redirect('search_employee')  # Redirect to a URL for viewing employee details

    return render(request, 'emp.html')

def view_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'view_employee.html', {'employee': employee})



def search_employee(request):
    query = request.GET.get('certificate_id')
    context = {
        'employee': None,
        'skills': None
    }
    if query:
        try:
            employee = Employee.objects.get(certificate_id=query)
            context['employee'] = employee
            context['skills'] = employee.skills.all()
        except Employee.DoesNotExist:
            pass  # Employee not found, context remains with None values

    return render(request, 'search_employee.html', context)

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


# def searchemp_api(request):
#     query = request.GET.get('certificate_id')
#     if query:
#         try:
#             employee = Employee.objects.get(certificate_id=query)
#             skills = list(employee.skills.all().values_list('skill', flat=True))
#             return JsonResponse({
#                 'employee': {
#                     'name': employee.name,
#                     'certificate_id': employee.certificate_id,
#                     'department_name': employee.department_name,
#                     'position': employee.position,
#                     'joining_date': employee.joining_date.strftime('%Y-%m-%d'),
#                     'leaving_date': employee.leaving_date.strftime('%Y-%m-%d') if employee.leaving_date else None,
#                     'worked_in': employee.worked_in,
#                     'tl_review': employee.tl_review,
#                     'dh_review': employee.dh_review,
#                     'feedback': employee.feedback
#                 },
#                 'skills': skills
#             })
#         except Employee.DoesNotExist:
#             return JsonResponse({'error': 'Employee not found'}, status=404)
#     return JsonResponse({'error': 'No certificate ID provided'}, status=400)
import base64
from django.http import JsonResponse

def searchemp_api(request):
    query = request.GET.get('certificate_id')
    if query:
        try:
            employee = Employee.objects.get(certificate_id=query)
            skills = list(employee.skills.all().values('skill', 'rating'))


            # Encode the image as base64
            if employee.image:
                with open(employee.image.path, "rb") as img_file:
                    image_data = base64.b64encode(img_file.read()).decode('utf-8')
            else:
                image_data = None

            if employee.certificate:
                with open(employee.certificate.path, "rb") as cert_file:
                    certificate_data = base64.b64encode(cert_file.read()).decode('utf-8')
            else:
                certificate_data = None

            return JsonResponse({
                'employee': {
                    'name': employee.name,
                    'certificate_id': employee.certificate_id,
                    'department_name': employee.department_name,
                    'position': employee.position,
                    'joining_date': employee.joining_date.strftime('%Y-%m-%d'),
                    'leaving_date': employee.leaving_date.strftime('%Y-%m-%d') if employee.leaving_date else None,
                    'worked_in': employee.worked_in,
                    'tl_review': employee.tl_review,
                    'dh_review': employee.dh_review,
                    'feedback': employee.feedback,
                    'image_data': image_data,
                    'certificate_data':certificate_data
                },
                'skills': skills
            })
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
    return JsonResponse({'error': 'No certificate ID provided'}, status=400)

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        # Update employee details
        employee.name = request.POST.get('name')
        employee.certificate_id = request.POST.get('certificate_id')
        employee.department_name = request.POST.get('department_name')
        employee.position = request.POST.get('position')
        employee.joining_date = request.POST.get('joining_date')
        employee.leaving_date = request.POST.get('leaving_date')
        employee.worked_in = request.POST.get('worked_in')
        employee.tl_review = request.POST.get('tl_review')
        employee.dh_review = request.POST.get('dh_review')
        employee.feedback = request.POST.get('feedback')
        
        # Update image if provided
        image = request.FILES.get('image')
        if image:
            employee.image = image
        
        employee.save()

        # Update skills
        skills_data = request.POST.getlist('skills')
        ratings_data = request.POST.getlist('ratings')
        employee.skills.all().delete()  # Remove existing skills
        for skill_data, rating_data in zip(skills_data, ratings_data):
            if skill_data:  # Making sure a skill name was actually provided
                Skill.objects.create(employee=employee, skill=skill_data, rating=int(rating_data))

        return redirect('view_employee_url', employee_id=employee_id)

    return render(request, 'edit_employee.html', {'employee': employee})


