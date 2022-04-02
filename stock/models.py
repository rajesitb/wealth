from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class CoAction(models.Model):
    stock_number = models.CharField(max_length=150, blank=True, null=True)
    stock_name = models.CharField(max_length=150, blank=True, null=True)
    stock_identity = models.CharField(max_length=150, blank=True, null=True)
    stock_id = models.CharField(max_length=150, blank=True, null=True)
    action_type = models.CharField(max_length=150, blank=True, null=True)
    action_date = models.DateField(blank=True, null=True)
    action_ratio = models.CharField(max_length=150, blank=True, null=True)
    agm_egm = models.DateField(blank=True, null=True)
    ex_date = models.DateField(blank=True, null=True)
    rd = models.DateField(blank=True, null=True)
    date_updated = models.DateField(auto_now=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True, help_text="remarks for your customers")
    recommendation = models.CharField(max_length=150, blank=True, null=True)
    buy_date = models.DateField(blank=True, null=True)
    exit_date = models.DateField(blank=True, null=True)
    buy_price = models.CharField(max_length=150, blank=True, null=True)
    exit_price = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f'Corporate action of {self.stock_name}'


class StockData(models.Model):
    company = models.ForeignKey(CoAction, on_delete=models.CASCADE, blank=True, null=True)
    stock_number = models.CharField(max_length=150, blank=True, null=True)
    stock_record = models.TextField()
    record_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'Stock data of {self.stock_number}'


class CorpActionRecord(models.Model):
    record_date = models.DateField()
    security_name = models.CharField(max_length=150, blank=True, null=True)
    security_id = models.CharField(max_length=150, blank=True, null=True)
    security_number = models.CharField(max_length=150, blank=True, null=True)
    message = models.CharField(max_length=450, blank=True, null=True)

    def __str__(self):
        return f'Corporate action record'


class UserPhone(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_phone', blank=True, null=True)
    mobile = models.CharField(verbose_name="Mobile Number", max_length=150, blank=True, null=True,
                              help_text='Enter your mobile number')
    agreement = models.BooleanField(default=False)
    mobile_verified = models.BooleanField(default=False)
    user_type = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f'UserPhone record of {self.mobile}'


class ScanData(models.Model):
    record_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'Last Scan at {self.record_date}'
