from django.db import models

# Create your models here.


class user_details(models.Model):
    username=models.CharField(max_length=200)
    age=models.IntegerField()
    Address=models.CharField(max_length=600)
    Gender=models.CharField(max_length=200)
    Mobile_number=models.IntegerField()
    Email=models.EmailField()
    Skills=models.CharField(max_length=900)
    profile_pic=models.ImageField(upload_to='profile_pic/',null=True,blank=True)
    company=models.CharField(max_length=200)
    experience=models.IntegerField()
    projects=models.CharField(max_length=900)
    position=models.CharField(max_length=200)
    certificates=models.CharField(max_length=1200)

    def __str__(self):

        return '{}' .format(self.username)



class registration(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    cpassword=models.CharField(max_length=200)

    def __str__(self):
        return '{}' .format(self.username)


class Login_user(models.Model):

    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return '{}' .format(self.username)



