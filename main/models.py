from django.db import models


class AllViews(models.Model):

    ip_address = models.GenericIPAddressField()

    class Meta:
        db_table = 'all_views'


class TodayView(models.Model):

    ip_address = models.GenericIPAddressField()

    class Meta:
        db_table = 'today_views'


class Users(models.Model):

    email = models.EmailField()
    password = models.CharField(max_length=255)
    private_key = models.CharField(max_length=255)
    created_at = models.CharField(max_length=64)

    class Meta:
        db_table = 'users'


class PremiumUsers(models.Model):

    chat_id = models.IntegerField()
    plan_type = models.CharField(max_length=16)
    buy_date = models.CharField(max_length=32)
    expire_date = models.CharField(max_length=32)
    status = models.CharField(max_length=12)

    class Meta:
        db_table = 'premium_user'


class PrivateKey(models.Model):

    token = models.CharField(max_length=255)
    chat_id = models.IntegerField()

    class Meta:
        db_table = 'private_key'


class UserUsage(models.Model):

    chat_id = models.IntegerField()
    usage_du = models.CharField(max_length=255)

    class Meta:
        db_table = 'user_usage'


class UserFileInfo(models.Model):

    chat_id = models.CharField(max_length=255)
    width = models.CharField(max_length=16)
    name = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=32)
    file_id = models.CharField(max_length=255)
    shortcode = models.CharField(max_length=32)
    caption = models.CharField(max_length=255)
    size = models.CharField(max_length=64)

    class Meta:
        db_table = 'file_information'


class PayInfo(models.Model):

    data = models.CharField(max_length=255)
    chat_id = models.IntegerField()
    amount = models.IntegerField()
    payeed = models.BooleanField()
    idpay_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'pay_data'


class UseMyAccount(models.Model):

    id = models.BigAutoField(primary_key=True)
    chat_id = models.IntegerField()
    status = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'use_my_account'


class UserWorks(models.Model):

    chat_id = models.IntegerField()
    url = models.CharField(max_length=255)

    class Meta:
        db_table = 'user_works'


class UserUsageU(models.Model):

    chat_id = models.IntegerField()
    usage_do = models.CharField(max_length=255)

    class Meta:
        db_table = 'user_usage'

