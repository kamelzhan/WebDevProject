# Generated by Django 3.2 on 2021-04-30 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210501_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='Department',
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('CourseId', models.AutoField(primary_key=True, serialize=False)),
                ('CourseName', models.CharField(max_length=100)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employees', to_field='EmployeeName')),
            ],
        ),
    ]
