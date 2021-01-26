from django.urls import path

from . import views

urlpatterns = [
    # Inicio
    path("", views.Home.as_view(), name="home"),
    # About
    path("acerca/", views.About.as_view(), name="about"),
    # Catastros Locales
    path("catastros-locales/", views.CatastroLocalList.as_view(), name="catastros_locales"),
    # Expedientes
    path("expedientes/", views.ExpedienteList.as_view(), name="expedientes"),
    path("expediente/<int:pk>/", views.ExpedienteDetail.as_view(), name="expediente"),
    # Personas
    path("personas/", views.PersonaList.as_view(), name="personas"),
    path("persona/<int:pk>/", views.PersonaDetail.as_view(), name="persona"),
    # Notas
    path("solicitud/", views.solicitud, name="solicitud"),
    path("visacion/", views.visacion, name="visacion"),
    # Búsquedas
    path("plano/", views.plano, name="buscar_plano"),
    path("set/", views.set, name="buscar_set"),
    path("catastro/", views.catastro, name="buscar_catastro"),
    # Herramientas
    path("caratula/", views.caratula, name="caratula"),
    path("dvapi/", views.dvapi, name="dvapi"),
    path("sie/", views.sie, name="sie"),
]
