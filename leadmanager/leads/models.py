from django.db import models
from django.utils.translation import gettext_lazy as _
#from django.core.validators import 


class Permission(models.Model):
    perm_name        = models.CharField(max_length=50, unique=True)
    perm_url         = models.SlugField(max_length=100)
    perm_create_at   = models.DateTimeField(auto_now_add=True)
    perm_modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.perm_name

class Role(models.Model):
    role_name        = models.CharField(max_length=50, unique=True)
    role_description = models.TextField(blank=True)
    role_create_at   = models.DateTimeField(auto_now_add=True)
    role_modified_at = models.DateTimeField(auto_now=True)
    role_permissions = models.ManyToManyField(Permission)
    def __str__(self):
        return self.role_name

class User(models.Model):
    class Status(models.IntegerChoices):
        INACTIVO = 0, _('Inactivos')
        ACTIVO   = 1, _('Activos')
        PAUSA    = 2, _('Vacaciones')
    user_user        = models.CharField(max_length=50, unique=True)
    user_password    = models.CharField(max_length=30)
    user_file        = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, default="images/noimage.jpg")
    user_status      = models.IntegerField(choices=Status.choices, default=Status.ACTIVO)
    user_create_at   = models.DateTimeField(auto_now_add=True)
    user_modified_at = models.DateTimeField(auto_now=True)
    user_role        = models.ForeignKey(Role, on_delete=models.CASCADE)
    def user_get_status(self):
        return self.Status(self.user_status).label
    def __str__(self):
        return self.user_user

class Lawyer(models.Model):
    class Status(models.IntegerChoices):
        INACTIVO = 0
        ACTIVO   = 1
        PAUSA    = 2
    lawy_name        = models.CharField(max_length=50) 
    lawy_last_name   = models.CharField(max_length=50)
    lawy_dni         = models.CharField(max_length=10, unique=True)
    lawy_email       = models.EmailField(unique=True, blank=True)   #null=True???
    lawy_phone       = models.CharField(max_length=20, blank=True)
    lawy_address     = models.CharField(max_length=100, blank=True)
    lawy_description = models.TextField(blank=True)
    lawy_tau         = models.CharField(max_length=20, unique=True)
    lawy_status      = models.IntegerField(choices=Status.choices, default=Status.ACTIVO)
    lawy_create_at   = models.DateTimeField(auto_now_add=True)
    lawy_modified_at = models.DateTimeField(auto_now=True)
    def lawy_get_status(self):
        return self.Status(self.lawy_status).label
    def __str__(self):
        return self.lawy_name + " " +self.lawy_last_name

class Assistant(models.Model):
    class Status(models.IntegerChoices):
        INACTIVO = 0
        ACTIVO   = 1
        PAUSA    = 2
    assi_name        = models.CharField(max_length=50) 
    assi_last_name   = models.CharField(max_length=50)
    assi_dni         = models.CharField(max_length=10, unique=True)
    assi_email       = models.EmailField(unique=True, blank=True)     #null=True???
    assi_phone       = models.CharField(max_length=20, blank=True)
    assi_address     = models.CharField(max_length=100, blank=True)
    assi_description = models.TextField(blank=True)
    assi_tau         = models.CharField(max_length=20, unique=True)
    assi_status      = models.IntegerField(choices=Status.choices, default=Status.ACTIVO)
    assi_create_at   = models.DateTimeField(auto_now_add=True)
    assi_modified_at = models.DateTimeField(auto_now=True)
    def assi_get_status(self):
        return self.Status(self.assi_status).label
    def __str__(self):
        return self.assi_name + " " + self.assi_last_name

class Client(models.Model):
    clie_name        = models.CharField(max_length=50)
    clie_last_name   = models.CharField(max_length=50)
    clie_dni         = models.CharField(max_length=10, unique=True)
    clie_email       = models.EmailField(unique=True, blank=True)      #null=True???
    clie_phone       = models.CharField(max_length=20, blank=True)
    clie_address     = models.CharField(max_length=100, blank=True)
    clie_create_at   = models.DateTimeField(auto_now_add=True)
    clie_modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.clie_name + " " + self.clie_last_name

class Type_case(models.Model):
    class Status(models.IntegerChoices):
        INACTIVO = 0
        ACTIVO   = 1
    type_name        = models.CharField(max_length=50, unique=True)
    type_description = models.TextField(blank=True)
    type_status      = models.IntegerField(choices=Status.choices, default=Status.ACTIVO)
    type_create_at   = models.DateTimeField(auto_now_add=True)
    type_modified_at = models.DateTimeField(auto_now=True)
    def type_get_status(self):
        return self.Status(self.type_status).label
    def __str__(self):
        return self.type_name

class Case(models.Model):
    class Status(models.IntegerChoices):
        INACTIVO = 0
        ACTIVO   = 1
        PAUSA    = 2
        GANADO   = 3
        PERDIDO  = 4
    case_code        = models.CharField(max_length=50, unique=True)
    case_name        = models.CharField(max_length=50)
    case_description = models.TextField(blank=True)
    case_status      = models.IntegerField(choices=Status.choices, default=Status.ACTIVO)
    case_start_date  = models.DateField()
    case_end_date    = models.DateField(blank=True, null=True)
    case_final_date  = models.DateField(blank=True, null=True)
    case_cost        = models.FloatField(blank=True, default=0)
    case_create_at   = models.DateTimeField(auto_now_add=True)
    case_modified_at = models.DateTimeField(auto_now=True)
    case_client      = models.ForeignKey(Client, on_delete=models.CASCADE)
    case_assistant   = models.ForeignKey(Assistant, on_delete=models.CASCADE)
    case_lawyer      = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    case_type        = models.ForeignKey(Type_case, on_delete=models.CASCADE)
    def case_get_status(self):
        return self.Status(self.case_status).label
    def __str__(self):
        return self.case_code + "-" + self.case_name

class Schedule(models.Model):
    class Status(models.IntegerChoices):
        CANCELADO   = 0
        ACTIVO      = 1
        PAUSA       = 2
        LOGRADO     = 3
        INCUMPLIDO  = 4
    sche_name        = models.CharField(max_length=50)
    sche_description = models.TextField(blank=True)
    sche_status      = models.IntegerField(choices=Status.choices, default=Status.ACTIVO)
    sche_color       = models.CharField(max_length=8, blank=True)
    sche_start       = models.DateTimeField()
    sche_duration    = models.IntegerField(blank=True, default=0)
    sche_create_at   = models.DateTimeField(auto_now_add=True)
    sche_modified_at = models.DateTimeField(auto_now=True)
    sche_case        = models.ForeignKey(Case, on_delete=models.CASCADE)
    def sche_get_status(self):
        return self.Status(self.sche_status).label
    def __str__(self):
        return self.sche_name + " " + self.Status(self.sche_status).label

class Record(models.Model):
    reco_name        = models.CharField(max_length=50)
    reco_description = models.TextField(blank=True)
    reco_file        = models.FileField(upload_to="documents/%Y/%m/%D/", blank=True, null=True)
    reco_date        = models.DateTimeField()
    reco_create_at   = models.DateTimeField(auto_now_add=True)
    reco_modified_at = models.DateTimeField(auto_now=True)
    reco_case        = models.ForeignKey(Case, on_delete=models.CASCADE)
    def __str__(self):
        return self.reco_name

class Payment(models.Model):
    paym_amount      = models.FloatField()
    paym_date        = models.DateTimeField()
    paym_create_at   = models.DateTimeField(auto_now_add=True)
    paym_modified_at = models.DateTimeField(auto_now=True)
    paym_case        = models.ForeignKey(Case, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.paym_case) + " / " + str(self.paym_amount)