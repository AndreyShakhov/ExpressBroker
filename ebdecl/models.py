from django.db import models
import datetime

greatdate = datetime.date.today()


class Decl(models.Model):
    decl_company_name = models.ForeignKey('Firm',on_delete=models.PROTECT, null=True, verbose_name='Название компании')
    decl_number = models.IntegerField(null=True, verbose_name='№ декларации')
    decl_tipe = models.ForeignKey('Decl_type',on_delete=models.PROTECT, null=True)
    decl_code_quantity = models.IntegerField(null=True)
    decl_car_number = models.CharField(max_length=100)
    decl_car_quantity = models.IntegerField(null=True)
    decl_price = models.IntegerField(null=True)
    decl_plament = models.ForeignKey('Payment_invoice_status',on_delete=models.PROTECT, null=True)
    decl_comment = models.TextField(null=True)
    decl_greatdate = models.DateField(default=greatdate)
    decl_status = models.ForeignKey('Decl_status',on_delete=models.PROTECT, null=True)


    class Meta:
        verbose_name = 'Декларации'
        verbose_name_plural = 'Декларации'
        ordering = ['decl_greatdate','decl_company_name'] #Сортировка



class Decl_type(models.Model):
    type_decl = models.CharField(max_length=30)

    def __str__(self):
        return self.type_decl

    class Meta:
        verbose_name = 'Тип декларации'
        verbose_name_plural = 'Тип декларации'

class Decl_status(models.Model):
    decl_status = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.decl_status

    class Meta:
        verbose_name = 'Статус декларации'
        verbose_name_plural = 'Статус декларации'


class Payment_invoice_status(models.Model):
    decl_status = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.decl_status

    class Meta:
        verbose_name = 'Статус счета'
        verbose_name_plural = 'Статус счета'

class Firm(models.Model):
    company_name = models.CharField(max_length=100,null=True)
    company_contact_person = models.CharField(max_length=100,null=True)
    company_phone = models.CharField(max_length=100,null=True)
    company_mail = models.EmailField(null=True)
    company_declpacked = models.IntegerField(null=True)
    company_ecp = models.BooleanField(null=True)
    company_ecp_decl = models.CharField(max_length=100,null=True)
    company_ecp_time = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'Компании'
        verbose_name_plural = 'компании'

    def __str__(self):
        return self.company_name

# Create your models here.
