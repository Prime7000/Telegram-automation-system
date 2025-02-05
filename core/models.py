from django.db import models

class robot(models.Model):
    robot_name = models.CharField(max_length=100, null=True, blank=True)
    organization_name = models.CharField(max_length=100)
    robot_key = models.CharField(max_length=500)

    def __str__(self):
        return self.organization_name if self.organization_name else f"Robot object: {self.id}"

class test(models.Model):
    message = models.CharField(max_length=10000,null=True, blank=True)
    img = models.ImageField(upload_to='products', null=True, blank=True)
    repeat = models.BooleanField(default=False)
    robot = models.ForeignKey(robot, on_delete=models.CASCADE, null=True, blank=True)
    time = models.CharField(max_length=100, default='')
    timeframe = models.CharField(max_length=50,default='weekly')


    def __str__(self):
        return self.message if self.message else f"Test object: {self.id}"
# Create your models here.
