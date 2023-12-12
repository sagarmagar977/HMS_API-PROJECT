from django.db import models

# Create your models here.

class menu(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    


class food(models.Model):
    name=models.CharField(max_length=200)
    menu=models.ForeignKey(menu,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    