from django.db import models

class Notebook(models.Model):
    STATUS=(
        ("new", "NEWEST"),
        ("old", "OLDEST"),
        ("title", "TITLE"),
    )
    head_title= models.CharField(max_length=100)
    text= models.TextField()
    time= models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=100 ,choices=STATUS, default = 'old')
    
    def __str__(self):
        return self.head_title
    