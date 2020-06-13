# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RptMonthlyPlan(models.Model):
    id_kvgs = models.UUIDField()
    month = models.IntegerField()
    year = models.IntegerField()
    production_plan = models.FloatField(blank=True, null=True)
    revenue_plan = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rpt_monthly_plan'


class RptOperators(models.Model):
    id_kvgs = models.UUIDField()
    report_datetime = models.DateField()
    sl_giao = models.FloatField(blank=True, null=True)
    sl_nhan = models.FloatField(blank=True, null=True)
    thoigian_chay_may = models.FloatField(blank=True, null=True)
    gia_bien_he_thong = models.FloatField(blank=True, null=True)
    gia_can = models.FloatField(db_column='gia_CAN', blank=True, null=True)  # Field name made lowercase.
    doanh_thu_du_kien = models.FloatField(blank=True, null=True)
    su_co_van_hanh = models.CharField(max_length=100, blank=True, null=True)
    su_kien_bat_thuong = models.CharField(max_length=100, blank=True, null=True)
    mn_tl = models.FloatField(blank=True, null=True)
    mn_hl = models.FloatField(blank=True, null=True)
    ll_ve_ho = models.FloatField(blank=True, null=True)
    ll_tuabin = models.FloatField(blank=True, null=True)
    ll_xa_tran = models.FloatField(blank=True, null=True)
    ll_xa_toi_thieu = models.FloatField(blank=True, null=True)
    w_hi = models.FloatField(blank=True, null=True)
    rp_hour = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rpt_operators'
        unique_together = (('id_kvgs', 'report_datetime', 'rp_hour'),)
