from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='midea/teacher/')
    full_name = models.CharField(max_length=250)
    job_Choose = (
        ('senior', 'senior'),
        ('middle', 'middle'),
        ('junior', 'junior'),
        ('ielts 9', 'ielts 9'),
        ('ielts 8.5', 'ielts 8.5'),
        ('ielts 8', 'ielts 8'),
        ('ielts 7.5', 'ielts 7.5'),
        ('ielts 7', 'ielts 7'),
        ('ielts 6.5', 'ielts 6.5'),
        ('ielts 5.5', 'ielts 5.5'),
        ('ielts 5', 'ielts 5'),
    )
    level = models.CharField(max_length=60, choices=job_Choose)
    phone_number = models.CharField(max_length=60)
    bio = models.TextField()
    work_years = models.IntegerField(default=0)
    instagram_link = models.CharField(max_length=250)
    telegram_link = models.CharField(max_length=250)

    def __str__(self):
        return self.full_name
