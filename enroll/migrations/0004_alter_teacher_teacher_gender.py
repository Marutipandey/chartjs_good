# Generated by Django 4.2.7 on 2024-01-20 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.student'),
        ),
    ]