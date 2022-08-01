from django.db import models

# Create your models here.
class Employee(models.Model):
    CHOICE=(('male','Male'), ('female',' Female'),('other','Others'))
    # fields of the model
    name=models.CharField(max_length=30)
    email=models.EmailField()
    date_of_birth=models.DateField()
    
    date_of_join=models.DateField()
    gender=models.CharField(max_length=20, choices=CHOICE )
    designation=models.CharField(max_length=30)
    reporting_manager=models.CharField(max_length=30)
    #img = models.ImageField(upload_to = "images/" )
        
    def __str__(self):
        return self.name
    

