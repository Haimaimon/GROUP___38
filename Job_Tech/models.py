from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.full_name}, {self.email},{self.password}'


class Job(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    company = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

