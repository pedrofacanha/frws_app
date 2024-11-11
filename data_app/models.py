from django.db import models

# 'worker' model
class Worker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
