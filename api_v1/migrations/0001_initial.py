# Generated by Django 5.0.2 on 2024-02-18 10:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='midea/teacher/')),
                ('full_name', models.CharField(max_length=250)),
                ('level', models.CharField(choices=[('senior', 'senior'), ('middle', 'middle'), ('junior', 'junior'), ('ielts 9', 'ielts 9'), ('ielts 8.5', 'ielts 8.5'), ('ielts 8', 'ielts 8'), ('ielts 7.5', 'ielts 7.5'), ('ielts 7', 'ielts 7'), ('ielts 6.5', 'ielts 6.5'), ('ielts 5.5', 'ielts 5.5'), ('ielts 5', 'ielts 5')], max_length=60)),
                ('phone_number', models.CharField(max_length=60)),
                ('bio', models.TextField()),
                ('work_years', models.IntegerField(default=0)),
                ('instagram_link', models.CharField(max_length=250)),
                ('telegram_link', models.CharField(max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
