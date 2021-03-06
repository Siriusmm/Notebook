from django.db import models

class User(models.Model):
    user_name=models.CharField(max_length=64,unique=True)
    user_password=models.CharField(max_length=128)
    user_email=models.EmailField(null=True)
    user_avatar=models.ImageField(null=True)

class Notes(models.Model):
    notes_user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    notes_title=models.CharField(max_length=300,default="无标题")
    note_content=models.TextField()
    notes_create_date=models.DateTimeField(auto_now_add=True)
    note_update_date=models.DateTimeField(auto_now=True)
