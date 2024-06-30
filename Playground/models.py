from django.db import models

# Create your models here.


class MainServices(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    
    
    def __str__(self):
        return self.name
    


class ServiceRequest(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    service = models.CharField(max_length=50)
    service_date = models.DateField()
    request = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.service}"
    
    
    
class OUR_TECHNICIANS(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    
    
    def __str__(self):
        return self.name
    
    
class Clients_reviews(models.Model):
    name = models.CharField(max_length=200)
    reviews = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    
    
    def __str__(self):
        return self.name
    
#list = ["TechSoftwareServices","HardwareServices","Plumbing",""]    
    
class ALLServices(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    
    
    def __str__(self):
        return self.name