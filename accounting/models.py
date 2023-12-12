from django.db import models
from frontdesk.models import GuestInfo


# Create your models here.

class bills(models.Model):
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE)
    total_amount = models.FloatField()

    def __str__(self):
        return f"{self.guest.f_name} {self.guest.l_name} - Total Amount: {self.total_amount}"

    
    
    
class payment(models.Model):
    bill=models.ForeignKey(bills,on_delete=models.CASCADE)
    paid_ampunt=models.FloatField()
    