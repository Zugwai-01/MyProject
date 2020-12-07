from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length = 264)
    last_name = models.CharField(max_length=264)
    student_ID=models.IntegerField(max_length=100,unique=True)
    email = models.EmailField(max_length=264,unique=True)
    Dept= models.ForeignKey('Department',on_delete=models.PROTECT,blank = True,null= True)
    Age= models.IntegerField(max_length = 2)




class Department(models.Model):
        Name_of_dept = models.CharField(max_length=264,unique=True)
        Faculty = models.CharField(max_length=264)





#class Staff(models.Model):
    #Staff_ID = models.CharField(max_length=100,unique=True)
    #Staff_last_name = models.CharField(max_length = 264)
    #Qualification=models.CharField(max_length = 264)
    #Dept=models.ForeignKey('Department',on_delete=models.PROTECT)



#class Courses(models.Model):
    #Course_code = models.CharField(max_length = 100,unique=True)
    #Course_name = models.CharField(max_length=128)
    #Dept = models.ForeignKey('Department',on_delete=models.PROTECT)
    #Units = models.IntegerField(max_length = 264)










# Create your models here.

# Create your models here.
