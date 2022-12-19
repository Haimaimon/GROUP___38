from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    company = models.CharField(max_length=50)

    def _str_(self):
        return f'{self.title}, {self.desc}, {self.company}'


class StudentJobs(models.Model):
    title = models.CharField(max_length=80)
    desc = models.TextField()
    company = models.CharField(max_length=40)
    location = models.CharField(max_length=30)

    def _str_(self):
        return f'{self.title}, {self.desc}, {self.company},{self.location}'