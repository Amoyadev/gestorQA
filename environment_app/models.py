from django.db import models


# Create your models here.
class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=45)
    vigencia_departamento = models.CharField(max_length=80)
    fecha_anulacion_departamento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'

class Hw(models.Model):
    id_hw = models.AutoField(primary_key=True)
    id_plataforma = models.ForeignKey('Plataforma', models.DO_NOTHING, db_column='id_plataforma')
    ip_hw = models.CharField(max_length=45)
    url_hw = models.CharField(max_length=45, blank=True, null=True)
    user_hw = models.CharField(max_length=45)
    password_hw = models.CharField(max_length=45)
    puerto_hw = models.CharField(max_length=45)
    direccion_fisica = models.CharField(max_length=45)
    vigencia_hw = models.CharField(max_length=80)
    fecha_anulacion_hw = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hw'


class Ip(models.Model):
    id_ip = models.AutoField(primary_key=True)
    id_sw = models.ForeignKey('Sw', models.DO_NOTHING, db_column='id_sw', blank=True, null=True)
    id_hw = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=45)
    puerto = models.CharField(max_length=45, blank=True, null=True)
    vigencia_sistema = models.CharField(max_length=80)
    fecha_anulacion_sistema = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ip'


class Modulo(models.Model):
    id_modulo = models.AutoField(primary_key=True)
    id_sistema = models.ForeignKey('Sistema', models.DO_NOTHING, db_column='id_sistema')
    nombre_modulo = models.CharField(max_length=45)
    vigencia_modulo = models.CharField(max_length=80)
    fecha_anulacion_modulo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo'


class Plataforma(models.Model):
    id_plataforma = models.AutoField(primary_key=True)
    id_modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='id_modulo')
    id_submodulo = models.ForeignKey('Submodulo', models.DO_NOTHING, db_column='id_submodulo', blank=True, null=True)
    id_sistema = models.ForeignKey('Sistema', models.DO_NOTHING, db_column='id_sistema')
    nombre_plataforma = models.CharField(max_length=45)
    tipo_ambiente_plataforma = models.CharField(max_length=45)
    tipo_servidor_plataforma = models.CharField(max_length=45)
    vigencia_plataforma = models.CharField(max_length=45)
    fecha_anulacion_plataforma = models.DateField(blank=True, null=True)
    tipo_motor_bd = models.CharField(max_length=45, blank=True, null=True)
    nombre_esquema_bd = models.CharField(max_length=45, blank=True, null=True)
    nombre_instancia_bd = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plataforma'


class Responsable(models.Model):
    id_responsable = models.AutoField(primary_key=True)
    id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_departamento')
    nombre_responsable = models.CharField(max_length=45, blank=True, null=True)
    vigencia_responsable = models.CharField(max_length=80)
    fecha_anulacion_responsable = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responsable'


class ResponsableSistema(models.Model):
    id_responsable = models.OneToOneField(Responsable, models.DO_NOTHING, db_column='id_responsable', primary_key=True)
    id_sistema = models.ForeignKey('Sistema', models.DO_NOTHING, db_column='id_sistema')

    class Meta:
        managed = False
        db_table = 'responsable_sistema'


class Sistema(models.Model):
    id_sistema = models.AutoField(primary_key=True)
    nombre_sistema = models.CharField(max_length=45)
    vigencia_sistema = models.CharField(max_length=80)
    fecha_anulacion_sistema = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sistema'


class Submodulo(models.Model):
    id_submodulo = models.AutoField(primary_key=True)
    id_modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='id_modulo')
    nombre_submodulo = models.CharField(max_length=45)
    vigencia_submodulo = models.CharField(max_length=80)
    fecha_anulacion_submodulo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'submodulo'


class Sw(models.Model):
    id_sw = models.AutoField(primary_key=True)
    id_plataforma = models.ForeignKey(Plataforma, models.DO_NOTHING, db_column='id_plataforma')
    endpoint_sw = models.CharField(max_length=45, blank=True, null=True)
    tipo_sw = models.CharField(max_length=45, blank=True, null=True)
    url_sw = models.CharField(max_length=45, blank=True, null=True)
    user_sw = models.CharField(max_length=45, blank=True, null=True)
    password_sw = models.CharField(max_length=45, blank=True, null=True)
    vigencia_sw = models.CharField(max_length=80, blank=True, null=True)
    fecha_anulacion_hw = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sw'

