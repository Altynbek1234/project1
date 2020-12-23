from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return  f'{self.title} > {self.date}'

