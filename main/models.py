from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
STATUS = (
    (0,"used"),
    (1,"new")
)
class Car(models.Model):
    car_name = models.CharField(max_length=200,)
    author = models.ForeignKey(User,on_delete= models.SET_NULL,null=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    car_image=models.ImageField(null=True,blank=True,default='/images/car.jpg')
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.car_name
