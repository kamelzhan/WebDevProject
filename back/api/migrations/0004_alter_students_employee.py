# Generated by Django 3.2 on 2021-04-29 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_students_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='api.employees'),
        ),
    ]
