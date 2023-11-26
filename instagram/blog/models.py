from django.db import models


class Index(models.Model):
    id = models.AutoField(primary_key=True)
    isim = models.CharField(max_length=25)
    soyisim= models.CharField(max_length=35)
    email=models.CharField(max_length=100)
    calistigibirim=models.CharField(max_length=45)
    maas = models.IntegerField()
  

    def __str__(self):
        return self.isim

class accounts(models.Model):
    accountid = models.IntegerField()
    userid = models.AutoField(primary_key=True)
    projeid=models.IntegerField()
    proje=models.CharField(max_length=225)
    dosyaadi=models.CharField(max_length=125)
    dosyatipi=models.CharField(max_length=20)
    dosyayol=models.CharField(max_length=300)
    yukledigikonu=models.CharField(max_length=300)
    yuklemetarih=models.DateField(auto_now=True)
    yuklemesaat=models.TimeField(auto_now=True)


class veriler(models.Model):
    kullaniciadi=models.CharField(max_length=30)
    sifre=models.CharField(max_length=60)
    


class MyFileModel(models.Model):
    file = models.FileField(upload_to='dosyalar/')  

    def __str__(self):
        return self.file.name