from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    public_data = models.DateTimeField()
    vote = models.DecimalField(max_digits=20, decimal_places=10)
    # vote = models.BigIntegerField()

# python manage.py makemigrations polls

class Economics(models.Model):
    title = models.CharField(max_length=100)
    href = models.CharField(max_length=100)
    create_date = models.DateTimeField(max_length=100)

# 문자는 CharField
# 소수점은 DecimalField