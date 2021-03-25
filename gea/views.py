from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic

from . import forms
from . import gea_vars as gv
from . import models


class CounterMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = self.get_queryset().count()
        return context


class SuccessDeleteMessageMixin:
    def delete(self, request, *args, **kwargs):
        delete_message = self.success_message if hasattr(self, "success_message") else "Objeto eliminado con éxito"
        messages.success(self.request, delete_message)
        return super().delete(request, *args, **kwargs)


class SearchMixin(object):
    def get_queryset(self):
        qset = super().get_queryset()
        q = self.request.GET.get("search")
        if q:
            q = q.split(" ")
            for w in q:
                qset = qset.filter(
                    Q(id__contains=w)
                    | Q(orden_numero__contains=w)
                    | Q(inscripcion_numero__contains=w)
                    | Q(expedientepartida__partida__pii__contains=w)
                    | Q(expedientepersona__persona__nombres__icontains=w)
                    | Q(expedientepersona__persona__apellidos__icontains=w)
                    | Q(expedientelugar__lugar__nombre__icontains=w)
                ).distinct()
        return qset


class ExpedienteAbiertoMixin(object):
    def get_queryset(self):
        qset = super().get_queryset()
        qset = qset.filter(Q(inscripcion_numero__isnull=True) & Q(cancelado=False) & Q(sin_inscripcion=False))[:10]
        return qset


class Home(LoginRequiredMixin, CounterMixin, SearchMixin, ExpedienteAbiertoMixin, generic.ListView):
    template_name = "index.html"
    model = models.Expediente

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # last 5 inscriptos
        context["insc_list"] = models.Expediente.objects.filter(
            Q(inscripcion_numero__isnull=False) & Q(inscripcion_fecha__isnull=False)
        ).order_by("-inscripcion_fecha", "inscripcion_numero")
        # ordenes pendientes
        context["ord_list"] = models.Expediente.objects.filter(
            Q(orden_numero__isnull=False) & Q(inscripcion_numero__isnull=True) & Q(orden_fecha__isnull=False)
        ).order_by("-orden_fecha", "orden_numero")
        # relevamientos
        context["relev_list"] = models.Expediente.objects.filter(fecha_medicion__isnull=False).order_by(
            "-fecha_medicion"
        )
        # altas
        context["open_list"] = models.Expediente.objects.filter(created__isnull=False).order_by("-created")
        return context


class About(generic.TemplateView):
    template_name = "about.html"


class ExpedienteMixin(object):
    def get_queryset(self):
        qset = super().get_queryset()
        q = self.request.GET.get("pendiente")
        if q:  # orden pendiente
            qset = qset.filter(Q(inscripcion_numero__isnull=q) & Q(orden_numero__isnull=not q))
        q = self.request.GET.get("inscripto")
        if q:  # plano inscripto
            qset = qset.filter(inscripcion_numero__isnull=False)
        else:
            qset = qset.filter(inscripcion_numero__isnull=True)
        q = self.request.GET.get("cancelado")
        if q:  # expediente cancelado
            qset = qset.filter(cancelado=q)
        q = self.request.GET.get("duplicado")
        if q:  # duplicado
            qset = qset.filter(duplicado=q)
        q = self.request.GET.get("sin_inscr")
        if q:  # sin inscripcion
            qset = qset.filter(sin_inscripcion=q)
        return qset


class ExpedienteListView(LoginRequiredMixin, CounterMixin, SearchMixin, generic.ListView):
    model = models.Expediente
    paginate_by = 10

    def get_paginate_by(self, queryset):
        """
        Paginate by specified value in querystring, or use default class
        property value.
        """
        return self.request.GET.get("paginate_by", self.paginate_by)


class ExpedienteDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Expediente


class NombreSearchMixin(object):
    def get_queryset(self):
        q = super().get_queryset()
        query = self.request.GET.get("search")
        query = "" if not query else query.split()
        for w in query:
            q = q.filter(
                Q(nombres__icontains=w)
                | Q(apellidos__icontains=w)
                | Q(nombres_alternativos__icontains=w)
                | Q(apellidos_alternativos__icontains=w)
                | Q(expedientepersona__expediente__id__contains=w)
                | Q(expedientepersona__expediente__inscripcion_numero__contains=w)
                | Q(expedientepersona__expediente__expedientepartida__partida__pii__contains=w)
                | Q(expedientepersona__expediente__expedientelugar__lugar__nombre__icontains=w)
            ).distinct()
        return q


class PersonaFilterMixin(object):
    def get_queryset(self):
        q = super().get_queryset()
        query = self.request.GET.get("search")
        query = "" if not query else query.split()
        for w in query:
            q = q.filter(
                Q(nombres__icontains=w)
                | Q(apellidos__icontains=w)
                | Q(nombres_alternativos__icontains=w)
                | Q(apellidos_alternativos__icontains=w)
                | Q(email__icontains=w)
                | Q(documento__contains=w)
                | Q(cuit_cuil__contains=w)
                | Q(telefono__contains=w)
                | Q(expedientepersona__expediente__id__contains=w)
            ).distinct()
        return q


# class PersonaListView(LoginRequiredMixin, NombreSearchMixin, CounterMixin, generic.ListView):
class PersonaListView(LoginRequiredMixin, PersonaFilterMixin, CounterMixin, generic.ListView):
    model = models.Persona
    paginate_by = 10

    def get_paginate_by(self, queryset):
        """
        Paginate by specified value in querystring, or use default class
        property value.
        """
        return self.request.GET.get("paginate_by", self.paginate_by)


class PersonaDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Persona


class PersonaCreateView(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = models.Persona
    form_class = forms.PersonaForm
    success_message = "¡Persona creada con éxito!"


class PersonaUpdateView(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = models.Persona
    form_class = forms.PersonaForm
    success_message = "¡Persona modificada con éxito!"


class PersonaDeleteView(SuccessDeleteMessageMixin, LoginRequiredMixin, generic.DeleteView):
    model = models.Persona
    success_url = reverse_lazy("personas")
    success_message = "Persona eliminada con éxito."


class LugarSearchMixin(object):
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("lugar")
        if q:
            return queryset.filter(expedientelugar__lugar__nombre=q)
        return queryset


class SeccionSearchMixin(object):
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("seccion")
        if q:
            return queryset.filter(expedientelugar__catastrolocal__seccion=q)
        return queryset


class ManzanaSearchMixin(object):
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("manzana")
        if q:
            return queryset.filter(expedientelugar__catastrolocal__manzana=q)
        return queryset


class ParcelaSearchMixin(object):
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("parcela")
        if q:
            return queryset.filter(expedientelugar__catastrolocal__parcela=q)
        return queryset


class CLMixin(object):
    def get_queryset(self):
        qset = super().get_queryset()
        q = self.request.GET.get("lugar")
        if q is not None:
            qset = qset.filter(expedientelugar__lugar__nombre=q).distinct()
        q = self.request.GET.get("seccion")
        if q is not None:
            qset = qset.filter(expedientelugar__catastrolocal__seccion=q)
        q = self.request.GET.get("manzana")
        if q is not None:
            qset = qset.filter(expedientelugar__catastrolocal__manzana=q)
        q = self.request.GET.get("parcela")
        if q is not None:
            qset = qset.filter(expedientelugar__catastrolocal__parcela=q)
        return qset


class CatastroLocalListView(LoginRequiredMixin, CounterMixin, CLMixin, generic.ListView):
    template_name = "gea/catastros_locales.html"
    model = models.Expediente
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lugar = self.request.GET.get("lugar")
        context["lugar"] = lugar
        s = self.request.GET.get("seccion")
        context["seccion"] = s
        m = self.request.GET.get("manzana")
        context["manzana"] = m
        p = self.request.GET.get("parcela")
        context["parcela"] = p
        context["lugares"] = models.Lugar.objects.values_list("nombre", flat=True).order_by("nombre")
        context["secciones"] = (
            models.CatastroLocal.objects.filter(expediente_lugar__lugar__nombre=lugar)
            .values_list("seccion", flat=True)
            .distinct()
            .order_by("seccion")
        )
        context["manzanas"] = (
            models.CatastroLocal.objects.filter(expediente_lugar__lugar__nombre=lugar)
            .filter(seccion=s)
            .values_list("manzana", flat=True)
            .distinct()
            .order_by("manzana")
        )
        context["parcelas"] = (
            models.CatastroLocal.objects.filter(expediente_lugar__lugar__nombre=lugar)
            .filter(Q(seccion=s) & Q(manzana=m))
            .values_list("parcela", flat=True)
            .distinct()
            .order_by("parcela")
        )
        return context


@login_required
def caratula(request):
    if request.method == "POST":  # If the form has been submitted...
        # CaratulaForm was defined in the previous section
        form = forms.CaratulaForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            #
            expediente_id = form.cleaned_data["expte_nro"]
            inmueble = form.cleaned_data["inmueble"]
            matricula = form.cleaned_data["matricula"]
            tomo = form.cleaned_data["tomo"]
            par = form.cleaned_data["par"]
            folio = form.cleaned_data["folio"]
            numero = form.cleaned_data["numero"]
            fecha = form.cleaned_data["fecha"]
            obs = form.cleaned_data["obs"]
            fmt = form.cleaned_data["fmt"]

            e = get_object_or_404(models.Expediente, id=expediente_id)
            template = loader.get_template("gea/tools/caratula.%s" % fmt)
            context = {
                "e": e,
                "inmueble": inmueble,
                "matricula": matricula,
                "tomo": tomo,
                "par": par,
                "folio": folio,
                "numero": numero,
                "fecha_dominio": fecha,
                "obs": obs,
                "fmt": fmt,
            }
            if fmt != "html":
                response = HttpResponse(template.render(context), content_type="image/x-%s" % fmt)
                cd = "attachment; filename=%04d-caratula.%s"
                response["Content-Disposition"] = cd % (expediente_id, fmt)
            else:
                return HttpResponse(template.render(context))
            return response
    else:
        form = forms.CaratulaForm()  # An unbound form

    return render(request, "gea/tools/caratula_form.html", {"form": form,})


@login_required
def solicitud(request):
    if request.method == "POST":  # If the form has been submitted...
        # SolicitudForm was defined in the previous section
        form = forms.SolicitudForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            expediente_id = form.cleaned_data["expte_nro"]
            circunscripcion = form.cleaned_data["circunscripcion"]
            domicilio_fiscal = form.cleaned_data["domicilio_fiscal"]
            # codigo_postal = form.cleaned_data['localidad']
            loc = form.cleaned_data["localidad"]
            localidad = gv.CP_dict[loc].split(" - ")[0]
            codigo_postal = gv.CP_dict[loc].split(" - ")[1]
            provincia = form.cleaned_data["provincia"]
            nota_titulo = form.cleaned_data["nota_titulo"]
            nota = form.cleaned_data["nota"]

            e = get_object_or_404(models.Expediente, id=expediente_id)
            template = loader.get_template("gea/doc/solic.html")
            context = {
                "e": e,
                "domfiscal": domicilio_fiscal,
                "circunscripcion": circunscripcion,
                "localidad": localidad,
                "cp": codigo_postal,
                "provincia": provincia,
                "nota_titulo": nota_titulo,
                "nota": nota,
            }
            return HttpResponse(template.render(context))
    else:
        form = forms.SolicitudForm()  # An unbound form

    return render(request, "gea/doc/solic_form.html", {"form": form,})


@login_required
def visacion(request):
    if request.method == "POST":  # If the form has been submitted...
        # VisacionForm was defined in the previous section
        form = forms.VisacionForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            eid = form.cleaned_data["expte_nro"]
            lugar = form.cleaned_data["lugar"]
            sr = gv.Lugar_dict[int(lugar)][0]
            localidad = gv.Lugar_dict[int(lugar)][1]

            e = get_object_or_404(models.Expediente, id=eid)
            # Redirect after POST
            return render(request, "gea/doc/visac.html", {"e": e, "sr": sr, "localidad": localidad},)
    else:
        form = forms.VisacionForm()  # An unbound form

    return render(request, "gea/doc/visac_form.html", {"form": form,})


@login_required
def plano(request):
    ftp_url = "ftp://zentyal.estudio.lan"
    if request.method == "POST":  # If the form has been submitted...
        form = forms.PlanoForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            circ = form.cleaned_data["circ"]
            nro = form.cleaned_data["n_insc"]
            return redirect("%s/planos/%s/%06d.pdf" % (ftp_url, circ, nro))
    else:
        form = forms.PlanoForm()  # An unbound form

    return render(request, "gea/search/plano_form.html", {"form": form,})


@login_required
def set(request):
    ftp_url = "ftp://zentyal.estudio.lan"
    if request.method == "POST":  # If the form has been submitted...
        form = forms.SetForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            pii = form.cleaned_data["partida"]
            sub_pii = form.cleaned_data["sub_pii"]
            url = "%s/set/%06d%04d.pdf" % (ftp_url, pii, sub_pii)
            return redirect(url)
    else:
        form = forms.SetForm()  # An unbound form

    return render(request, "gea/search/set_form.html", {"form": form,})


def get_dvapi(dp, ds, sd, pii, subpii):
    coef = "9731"
    _coef = coef + coef + coef + coef
    strpii = "%02d%02d%02d%06d%04d" % (dp, ds, sd, pii, subpii)
    suma = 0
    for i in range(0, len(strpii)):
        m = str(int(strpii[i]) * int(_coef[i]))
        suma += int(m[len(m) - 1])
    return (10 - (suma % 10)) % 10


def dvapi(request):
    if request.method == "POST":  # If the form has been submitted...
        form = forms.DVAPIForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            dp = form.cleaned_data["dp"]
            ds = form.cleaned_data["ds"]
            sd = form.cleaned_data["sd"]
            pii = form.cleaned_data["partida"]
            sub_pii = form.cleaned_data["sub_pii"]
            dv = get_dvapi(dp, ds, sd, pii, sub_pii)
            return render(request, "gea/tools/dvapi_form.html", {"dv": dv, "form": form},)
    else:
        form = forms.DVAPIForm()  # An unbound form

    return render(request, "gea/tools/dvapi_form.html", {"form": form,})


def sie(request):
    if request.method == "POST":  # If the form has been submitted...
        form = forms.SIEForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            mesa = form.cleaned_data["mesa"]
            nro = form.cleaned_data["nro"]
            dv = form.cleaned_data["digito"]
            # dv = get_dvsie(mesa, nro)
            base_url = "https://www.santafe.gov.ar/index.php/apps/sie"
            param = "?mesa=%d&numero=%d&digito=%d&tipoSIE=1" % (mesa, nro, dv)
            url = "".join([base_url, param])
            return redirect(url)
    else:
        form = forms.SIEForm()  # An unbound form

    return render(request, "gea/tools/sie_form.html", {"form": form,})


@login_required
def catastro(request):
    if request.method == "POST":  # If the form has been submitted...
        # VisacionForm was defined in the previous section
        form = forms.CLForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            lugar = form.cleaned_data["lugar"]
            seccion = form.cleaned_data["seccion"]
            manzana = form.cleaned_data["manzana"]
            parcela = form.cleaned_data["parcela"]

            filtro = "?"
            if lugar is not None:
                filtro = "%s%s%s" % (filtro, "&expedientelugar__lugar__nombre=", lugar,)
            if seccion != "":
                filtro = "%s%s%s" % (filtro, "&expedientelugar__catastrolocal__seccion=", seccion,)
            if manzana != "":
                filtro = "%s%s%s" % (filtro, "&expedientelugar__catastrolocal__manzana=", manzana,)
            if parcela != "":
                filtro = "%s%s%s" % (filtro, "&expedientelugar__catastrolocal__parcela=", parcela,)
            # Redirect after POST
            return redirect("/admin/gea/expediente/%s" % filtro)
    else:
        form = forms.CLForm()  # An unbound form

    return render(request, "gea/search/catastro_form.html", {"form": form,})


# #####
# ##### EXPERIMENTAL
# #####
# from calendar import HTMLCalendar
# from datetime import date
# from itertools import groupby
#
# from django.utils.html import conditional_escape as esc


# class QuerysetCalendar(HTMLCalendar):
#
#     def __init__(self, queryset, datefield):
#         self.datefield = datefield
#         super(QuerysetCalendar, self).__init__()
#         self.queryset_by_date = self.group_by_day(queryset)
#
#     def formatday(self, day, weekday):
#         if day != 0:
#             cssclass = self.cssclasses[weekday]
#             if date.today() == date(self.year, self.month, day):
#                 cssclass += ' today'
#             if day in self.queryset_by_date:
#                 cssclass += ' filled'
#                 body = ['<ul>']
#                 for item in self.queryset_by_date[day]:
#                     body.append('<li>')
#                     body.append('<a href="%s">' % item.get_absolute_url())
#                     body.append(esc(item))
#                     body.append('</a></li>')
#                 body.append('</ul>')
#                 return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
#             return self.day_cell(cssclass, day)
#         return self.day_cell('noday', ' ')
#
#     def formatmonth(self, year, month):
#         self.year, self.month = year, month
#         return super(QuerysetCalendar, self).formatmonth(year, month)
#
#     def group_by_day(self, queryset):
#         field = lambda item: getattr(item, self.datefield).day
#         return dict(
#             [(day, list(items)) for day, items in groupby(queryset, field)]
#         )
#
#     def day_cell(self, cssclass, body):
#         return '<td class="%s">%s</td>' % (cssclass, body)


# ######
# from django.utils.safestring import mark_safe
#
#
# @login_required
# def calendar(request, year, month):
#     e = models.Expediente.objects.order_by('fecha_medicion').filter(
#         fecha_medicion__year=year, fecha_medicion__month=month
#         )
#     cal = QuerysetCalendar(e, 'fecha_medicion').formatmonth(int(year),
#                                                             int(month))
#     return render_to_response('gea/tools/calendar.html',
#                               {'calendar': mark_safe(cal), })
