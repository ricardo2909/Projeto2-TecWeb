from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    id = models.BigAutoField(primary_key=True)
    
    def __str__(self): 
        return '{0}.{1}'.format(self.id, self.title)
