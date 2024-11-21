from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ResponseCodeModel(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=102)
  creation_date = models.DateField(auto_now_add=True)
  response_codes = models.TextField()
  image_links = models.TextField()

  def __str__(self):
    return self.name
