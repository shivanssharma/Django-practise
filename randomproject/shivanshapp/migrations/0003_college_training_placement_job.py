# Generated by Django 4.2.6 on 2023-10-12 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shivanshapp', '0002_student_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='college',
            fields=[
                ('college_id', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('name_of_college', models.TextField(max_length=200)),
                ('state', models.TextField(max_length=100)),
                ('city', models.TextField(max_length=100)),
                ('courses', models.TextField(max_length=100)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shivanshapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='training',
            fields=[
                ('training_id', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('training_name', models.TextField(max_length=200)),
                ('training_period', models.IntegerField(max_length=200)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shivanshapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='placement',
            fields=[
                ('placement_id', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('qualification_requirement', models.TextField(max_length=200)),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shivanshapp.college')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shivanshapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('job_id', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('company_name', models.TextField(max_length=200)),
                ('job_name', models.TextField(max_length=200)),
                ('salary', models.IntegerField(max_length=100)),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shivanshapp.college')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shivanshapp.student')),
            ],
        ),
    ]
