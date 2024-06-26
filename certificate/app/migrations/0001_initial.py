# Generated by Django 3.2.6 on 2024-04-23 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=100)),
                ('certificate_id', models.CharField(max_length=200)),
                ('department_name', models.CharField(max_length=200)),
                ('joining_date', models.DateField()),
                ('leaving_date', models.DateField()),
                ('worked_in', models.TextField()),
                ('tl_review', models.TextField()),
                ('dh_review', models.TextField()),
                ('feedback_review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='app.employee')),
            ],
        ),
    ]
