from django.db import models


# Create your models here.

class GuestInfo(models.Model):
    f_name=models.CharField(max_length=100)
    l_name=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    # phone_number=models.IntegerField()
    phone_number = models.IntegerField(default=None,null=True) 
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.f_name
    

class roomtype(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class room(models.Model):
    room_status=[('occupied','occupied'),('available','available')]
    room_no=models.IntegerField(default=None,null=True)
    description=models.TextField(max_length=300)
    status=models.CharField(max_length=20,choices=room_status)
    floor=models.CharField(max_length=20)
    room_type=models.ForeignKey(roomtype,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.room_no)

class guestroom(models.Model):
    guest=models.ForeignKey(GuestInfo,on_delete=models.CASCADE)
    room_no=models.ForeignKey(room,on_delete=models.CASCADE)
    checked_out=models.BooleanField(default=False)
    def __str__(self):
        return str(self.room_no)
        
    

    