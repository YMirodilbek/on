from django.db import models


class A(models.Model):
    deys = models.CharField(max_length=200)
    raqami = models.IntegerField()
    yil = models.CharField(max_length=300)
    yil2 = models.CharField(max_length=200)
    raqami2 = models.CharField(max_length=200)
    stranasi = models.CharField(max_length=300)
    f_qoshish = models.CharField(max_length=400)
    l_qoshish = models.CharField(max_length=500)
    ochestva_qoshish = models.CharField(max_length=500)
    rojdeniya_qoshish = models.CharField(max_length=500)
    adres_qoshish = models.TextField()
    
    def str(self):
        return self.deys