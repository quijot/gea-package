from django import forms

from . import gea_vars as gv
from . import models


class CaratulaForm(forms.Form):
    expte_nro = forms.IntegerField(label="Expediente Nº", widget=forms.NumberInput(attrs={"placeholder": "ej: 4300"}),)
    inmueble = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "ej: Una fracción de terreno..."}), required=False,
    )
    matricula = forms.IntegerField(required=False)
    tomo = forms.IntegerField(required=False)
    par = forms.BooleanField(required=False)
    folio = forms.IntegerField(required=False)
    numero = forms.IntegerField(label="Número", required=False)
    fecha = forms.DateField(required=False)
    obs = forms.CharField(
        label="Observaciones",
        widget=forms.Textarea(
            attrs={
                "placeholder": "ej: Modifica el Lote Nº 1 del \
                              Plano Nº 23.456. Etc."
            }
        ),
        required=False,
    )
    FORMAT_CHOICES = (
        ("html", "HTML"),
        ("dxf", "DXF"),
    )
    fmt = forms.ChoiceField(label="Formato de salida", choices=FORMAT_CHOICES)


class SolicitudForm(forms.Form):
    expte_nro = forms.IntegerField(label="Expediente Nº", widget=forms.NumberInput(attrs={"placeholder": "ej: 4300"}),)
    circunscripcion = forms.ChoiceField(label="Circunscripción", choices=gv.CIRC, initial=gv.CIRC_DEFAULT)
    domicilio_fiscal = forms.CharField(
        max_length=40, widget=forms.TextInput(attrs={"placeholder": "ej: San Martín 430"}),
    )
    localidad = forms.ChoiceField(choices=gv.CP, initial=gv.CP_DEFAULT)
    provincia = forms.ChoiceField(choices=gv.PROV, initial=gv.PROV_DEFAULT)
    nota_titulo = forms.ChoiceField(label="Nota título", choices=gv.NOTA)
    nota = forms.CharField(
        label="Nota contenido",
        widget=forms.Textarea(attrs={"placeholder": "Ingrese el texto de la nota correspondiente"}),
        required=False,
    )


class VisacionForm(forms.Form):
    expte_nro = forms.IntegerField(label="Expediente Nº")
    lugar = forms.ChoiceField(choices=gv.LUGAR, initial=0)


#
# Buscar Plano por Nro
#
class PlanoForm(forms.Form):
    circ = forms.IntegerField(label="Circunscripción", min_value=1, max_value=2, initial=1)
    n_insc = forms.IntegerField(label="Plano Nº", min_value=1, max_value=999999)


#
# Buscar Set de Datos por PII
#
class SetForm(forms.Form):
    partida = forms.IntegerField(min_value=1, max_value=999999)
    sub_pii = forms.IntegerField(label="Subpartida", min_value=0, max_value=9999, initial=0)


#
# Calcular Digito Verificador de la PII
#
class DVAPIForm(forms.Form):
    dp = forms.IntegerField(label="DP (departamento)", min_value=1, max_value=19, initial=11)
    ds = forms.IntegerField(label="DS (distrito)", min_value=1, max_value=99, initial=8)
    sd = forms.IntegerField(label="SD (subdistrito)", min_value=0, max_value=99, initial=0)
    partida = forms.IntegerField(min_value=1, max_value=999999)
    sub_pii = forms.IntegerField(label="Subpartida", min_value=0, max_value=9999, initial=0)


#
# Consultar estado en Sistema de Información de Expedientes del SCIT
#
class SIEForm(forms.Form):
    mesa = forms.IntegerField(min_value=13401, max_value=13401, initial=13401)
    nro = forms.IntegerField(label="Número", min_value=1, max_value=9999999)
    digito = forms.IntegerField(label="Dígito", min_value=0, max_value=9, initial=0)


#
#
# Exptes x Catastro Local
#
#
class CLForm(forms.Form):
    lugar = forms.ModelChoiceField(
        queryset=models.Lugar.objects.exclude(nombre__startswith="Colonia")
        .exclude(nombre__startswith="Zona Rural")
        .exclude(nombre__startswith="Zona de Islas"),
        required=False,
    )
    seccion = forms.CharField(max_length=4, required=False)
    manzana = forms.CharField(max_length=4, required=False)
    parcela = forms.CharField(max_length=4, required=False)
