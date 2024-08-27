from django.db import models

class COR(models.Model):
    ds_cor = models.CharField(max_length=50, unique=True)

class VEICULO_MARCA(models.Model):
    ds_marca_veiculo = models.CharField(max_length=50, unique=True)

class VEICULO_TIPO(models.Model):
    ds_tipo_veiculo = models.CharField(max_length=50)

class VEICULO(models.Model):
    marca_veiculo = models.ForeignKey(VEICULO_MARCA, on_delete=models.CASCADE)
    ds_modelo_veiculo = models.CharField(max_length=50)
    tipo_veiculo = models.ForeignKey(VEICULO_TIPO, on_delete=models.DO_NOTHING)

class VEICULO_PLACA(models.Model):
    ds_placa_veiculo = models.CharField(max_length=50, unique=True)

class VESTIMENTA(models.Model):
    ds_vestimenta = models.CharField(max_length=50, unique=True)

class VESTIMENTA_ESTAMPA(models.Model):
    ds_estampa_vestimenta = models.CharField(max_length=50, unique=True)

class LOCAL_TATUAGEM(models.Model):
    ds_local_tatuagem = models.CharField(max_length=50, unique=True)

class CABELO_TIPO(models.Model):
    ds_tipo_cabelo = models.CharField(max_length=50, unique=True)

class CABELO_COMPRIMENTO(models.Model):
    ds_comprimento_cabelo = models.CharField(max_length=50, unique=True)

class CABELO_COR(models.Model):
    ds_cor_cabelo = models.CharField(max_length=50, unique=True)

class SITUACAO(models.Model):
    ds_situacao = models.CharField(max_length=50)

class RISP(models.Model):
    ds_risp = models.CharField(max_length=100, unique=True)
    situacao = models.ForeignKey(SITUACAO, on_delete=models.CASCADE)

class MUNICIPIOS(models.Model):
    ds_municipio = models.CharField(max_length=50, unique=True)
    risp = models.ForeignKey(RISP, on_delete=models.DO_NOTHING)
    situacao = models.ForeignKey(SITUACAO, on_delete=models.CASCADE)

class DISTRITOS_POVOADOS(models.Model):
    ds_distrito_povoado = models.CharField(max_length=50)
    municipio = models.ForeignKey(MUNICIPIOS, on_delete=models.DO_NOTHING, blank=True, null=True)
    situacao = models.ForeignKey(SITUACAO, on_delete=models.CASCADE)

class AISP(models.Model):
    ds_aisp = models.CharField(max_length=50, unique=True)
    risp = models.ForeignKey(RISP,on_delete=models.CASCADE)
    situacao = models.ForeignKey(SITUACAO, on_delete=models.CASCADE)

class BAIRROS(models.Model):
    municipio = models.ForeignKey(MUNICIPIOS, on_delete=models.DO_NOTHING)
    distrito = models.ForeignKey(DISTRITOS_POVOADOS, on_delete=models.DO_NOTHING, blank=True, null=True)
    ds_bairro = models.CharField(max_length=50)
    aisp = models.ForeignKey(AISP,on_delete=models.DO_NOTHING, blank=True, null=True)
    situacao = models.ForeignKey(SITUACAO, on_delete=models.CASCADE)

class BOP_TATUAGEM(models.Model):
    nro_bop = models.CharField(max_length=50)
    local_tatuagem = models.ForeignKey(LOCAL_TATUAGEM,on_delete=models.DO_NOTHING)

class BOP_VEICULO(models.Model):
    nro_bop = models.CharField(max_length=50)
    veiculo = models.ForeignKey(VEICULO,on_delete=models.DO_NOTHING, blank=True, null=True)
    cor = models.ForeignKey(COR,on_delete=models.DO_NOTHING, blank=True, null=True)


class BOP_PLACA_VEICULO(models.Model):
    nro_bop = models.CharField(max_length=50)
    placa_veiculo = models.ForeignKey(VEICULO_PLACA,on_delete=models.DO_NOTHING)

class BOP_CABELO(models.Model):
    nro_bop = models.CharField(max_length=50)
    tipo_cabelo = models.ForeignKey(CABELO_TIPO,on_delete=models.DO_NOTHING, blank=True, null=True)
    cor_cabelo = models.ForeignKey(CABELO_COR,on_delete=models.DO_NOTHING, blank=True, null=True)
    comprimento_cabelo = models.ForeignKey(CABELO_COMPRIMENTO,on_delete=models.DO_NOTHING, blank=True, null=True)

class BOP(models.Model):
    nro_bop = models.CharField(max_length=50, unique=True)
    data_registro = models.DateTimeField()
    data_fato = models.DateTimeField()
    registro = models.CharField(max_length=100)
    relato = models.TextField()
    bairro = models.ForeignKey(BAIRROS, on_delete=models.DO_NOTHING, blank=True, null=True)
    distrito = models.ForeignKey(DISTRITOS_POVOADOS, on_delete=models.DO_NOTHING, blank=True, null=True)
    municipio = models.ForeignKey(MUNICIPIOS, on_delete=models.DO_NOTHING)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    bop_tatuagem = models.ForeignKey(BOP_TATUAGEM, on_delete=models.CASCADE, blank=True, null=True)
    bop_cabelo = models.ForeignKey(BOP_CABELO, on_delete=models.CASCADE, blank=True, null=True)

class BOP_VESTIMENTA(models.Model):
    nro_bop = models.ForeignKey(BOP, on_delete=models.CASCADE)
    vestimenta = models.ForeignKey(VESTIMENTA, on_delete=models.DO_NOTHING, blank=True, null=True)
    cor = models.ForeignKey(COR, on_delete=models.DO_NOTHING, blank=True, null=True)
    estampa = models.ForeignKey(VESTIMENTA_ESTAMPA, on_delete=models.DO_NOTHING, blank=True, null=True)