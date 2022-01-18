from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}: {self.content}\n{self.number}'
    
