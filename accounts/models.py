from django.db import models
class student(models.Model):

    regid=models.CharField(max_length=200,null=False,primary_key=True)
    name=models.CharField(max_length=200,null=False)
    email=models.CharField(max_length=200,null=True)
    date_of_join=models.DateTimeField(auto_now_add=True,null=True)
    gender=models.CharField(max_length=10,null=True,choices=(("male","male"),("female","female")))

    def __str__(self):
        return (self.name+" -regno :-"+self.regid)
class marks(models.Model) :
    regid=models.ForeignKey(student,on_delete=models.CASCADE)
    physics=models.IntegerField(null=True)
    maths=models.IntegerField(null=True)
    science=models.IntegerField(null=True)
    social=models.IntegerField(null=True)
    english=models.IntegerField(null=True)
    total=models.IntegerField(null=True)
    def __str__(self):
        return (self.regid)
        
   
   