from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.
class msg_user(models.Model):
    nombre = models.CharField(max_length=200)
    mail   = models.EmailField(max_length=200)
    asunto = models.CharField(max_length=200)
    mensaje= models.TextField()