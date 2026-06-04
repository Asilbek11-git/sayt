from django.db import models

class Muallif(models.Model):
    ism=models.CharField(max_length=130)
    tugilgan_yili=models.IntegerField()
    davlat=models.CharField(max_length=130)


    def __str__(self):
        return self.ism


class Janr(models.Model):
    nomi=models.CharField(max_length=100,unique = True)


    def __str__(self):
        return self.nomi





class Kitob(models.Model):
    nomi = models.CharField(max_length=200)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    janrlar = models.ManyToManyField(Janr)
    til = models.CharField(max_length=2, default='uz')
    nashr_yili = models.IntegerField()
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    mavjud = models.BooleanField(default=True)
    qoshilgan_sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi




class KitobNusxa(models.Model):
    kitob=models.ForeignKey(Kitob, on_delete=models.CASCADE)
    integral_raqam = models.CharField(max_length=200)
    holat=models.CharField(max_length=200)
    


class Ijara(models.Model):
    nusxa=models.ForeignKey(KitobNusxa, on_delete=models.CASCADE)
    oluvchi=models.CharField(max_length=200)
    olingan_sana = models.DateField()
    qaytarilgan=models.BooleanField(default=True)


    

