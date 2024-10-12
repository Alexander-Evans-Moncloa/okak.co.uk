from django.db import models

class UserData(models.Model):
    first_name = models.CharField(max_length=100, default="N/A")
    last_name = models.CharField(max_length=100, default="N/A")
    email = models.EmailField(max_length=500, default="N/A")
    address_line1 = models.CharField(max_length=255, default="N/A")
    address_line2 = models.CharField(max_length=255, blank=True, null=True, default='')
    city = models.CharField(max_length=100, default="N/A")
    postal_code = models.CharField(max_length=20, default="N/A")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
