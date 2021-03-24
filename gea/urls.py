from django.urls import path

from . import views

urlpatterns = [
    # Inicio
    path("", views.Home.as_view(), name="home"),
    # About
    path("acerca/", views.About.as_view(), name="about"),
    # Catastros Locales
    path("catastros-locales/", views.CatastroLocalListView.as_view(), name="catastros_locales"),
    # Expedientes
    path("expedientes/", views.ExpedienteListView.as_view(), name="expedientes"),
    path("expediente/<int:pk>/", views.ExpedienteDetailView.as_view(), name="expediente"),
    # Personas
    path("personas/", views.PersonaListView.as_view(), name="personas"),
    path("persona/<int:pk>/", views.PersonaDetailView.as_view(), name="persona"),
    path("persona/crear/", views.PersonaCreateView.as_view(), name="persona_create"),
    path("persona/editar/<int:pk>/", views.PersonaUpdateView.as_view(), name="persona_update"),
    path("persona/borrar/<int:pk>/", views.PersonaDeleteView.as_view(), name="persona_delete"),
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
