from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    mail=models.CharField(max_length=200)
    message=models.TextField(max_length=800)
    
    class Meta:
        verbose_name=("Contact")
        verbose_name_plural=("Contacts")
    
    def __str__(self):
        return self.name
