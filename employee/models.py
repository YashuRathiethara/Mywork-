from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    eid = models.CharField(max_length=15)
    ename = models.CharField(max_length=15)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    
    class Meta:
        db_table = "employee"
        