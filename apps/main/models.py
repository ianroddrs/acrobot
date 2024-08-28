from django.db import models

class Aisp(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_aisp = models.CharField(unique=True, max_length=50)
    situacao = models.ForeignKey('Situacao', models.DO_NOTHING)
    risp = models.ForeignKey('Risp', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'database_aisp'


class Bairros(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_bairro = models.CharField(max_length=50)
    situacao = models.ForeignKey('Situacao', models.DO_NOTHING)
    aisp = models.ForeignKey(Aisp, models.DO_NOTHING, blank=True, null=True)
    distrito = models.ForeignKey('DistritosPovoados', models.DO_NOTHING, blank=True, null=True)
    municipio = models.ForeignKey('Municipios', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'database_bairros'


class Bop(models.Model):
    id = models.BigAutoField(primary_key=True)
    nro_bop = models.CharField(unique=True, max_length=50)
    data_registro = models.DateTimeField()
    data_fato = models.DateTimeField()
    registro = models.ForeignKey('Registros', models.DO_NOTHING)
    relato = models.TextField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    bairro = models.ForeignKey(Bairros, models.DO_NOTHING, blank=True, null=True)
    distrito = models.ForeignKey('DistritosPovoados', models.DO_NOTHING, blank=True, null=True)
    municipio = models.ForeignKey('Municipios', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'database_bop'


class BopCabelo(models.Model):
    id = models.BigAutoField(primary_key=True)
    comprimento_cabelo = models.ForeignKey('CabeloComprimento', models.DO_NOTHING, blank=True, null=True)
    cor_cabelo = models.ForeignKey('CabeloCor', models.DO_NOTHING, blank=True, null=True)
    nro_bop = models.CharField(max_length=50)
    tipo_cabelo = models.ForeignKey('CabeloTipo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'database_bop_cabelo'


class BopPlacaVeiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nro_bop = models.CharField(max_length=50)
    placa_veiculo = models.ForeignKey('VeiculoPlaca', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'database_bop_placa_veiculo'


class BopTatuagem(models.Model):
    id = models.BigAutoField(primary_key=True)
    local_tatuagem = models.ForeignKey('LocalTatuagem', models.DO_NOTHING)
    nro_bop = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'database_bop_tatuagem'


class BopVeiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    cor = models.ForeignKey('Cor', models.DO_NOTHING, blank=True, null=True)
    nro_bop = models.CharField(max_length=50)
    veiculo = models.ForeignKey('Veiculo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'database_bop_veiculo'


class BopVestimenta(models.Model):
    id = models.BigAutoField(primary_key=True)
    cor = models.ForeignKey('Cor', models.DO_NOTHING, blank=True, null=True)
    estampa = models.ForeignKey('VestimentaEstampa', models.DO_NOTHING, blank=True, null=True)
    nro_bop = models.CharField(max_length=50)
    vestimenta = models.ForeignKey('Vestimenta', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'database_bop_vestimenta'


class CabeloComprimento(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_comprimento_cabelo = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'database_cabelo_comprimento'


class CabeloCor(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_cor_cabelo = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'database_cabelo_cor'


class CabeloTipo(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_tipo_cabelo = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'database_cabelo_tipo'


class Cor(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_cor = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'database_cor'


class DistritosPovoados(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_distrito_povoado = models.CharField(max_length=50)
    situacao = models.ForeignKey('Situacao', models.DO_NOTHING)
    municipio = models.ForeignKey('Municipios', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'database_distritos_povoados'


class LocalTatuagem(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_local_tatuagem = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'database_local_tatuagem'


class Municipios(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_municipio = models.CharField(unique=True, max_length=50)
    situacao = models.ForeignKey('Situacao', models.DO_NOTHING)
    risp = models.ForeignKey('Risp', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'database_municipios'


class Registros(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_registro = models.CharField(unique=True, max_length=500)
    situacao = models.ForeignKey('Situacao', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'database_registros'


class Risp(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_risp = models.CharField(unique=True, max_length=100)
    situacao = models.ForeignKey('Situacao', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'database_risp'


class Situacao(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_situacao = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'database_situacao'


class Veiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_modelo_veiculo = models.CharField(max_length=50)
    marca_veiculo = models.ForeignKey('VeiculoMarca', models.DO_NOTHING)
    tipo_veiculo = models.ForeignKey('VeiculoTipo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'database_veiculo'


class VeiculoMarca(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_marca_veiculo = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'database_veiculo_marca'


class VeiculoPlaca(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_placa_veiculo = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'database_veiculo_placa'


class VeiculoTipo(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_tipo_veiculo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'database_veiculo_tipo'


class Vestimenta(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_vestimenta = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'database_vestimenta'


class VestimentaEstampa(models.Model):
    id = models.BigAutoField(primary_key=True)
    ds_estampa_vestimenta = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'database_vestimenta_estampa'
