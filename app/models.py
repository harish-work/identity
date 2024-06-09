from django.db import models

# Create your models here.
class Identity(models.Model):
    id = models.AutoField(primary_key=True)
    phoneNumber = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    linkedID = models.IntegerField(null=True)
    linkprecedence = models.CharField(max_length=10,default='primary')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
