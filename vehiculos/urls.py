# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from vehiculos.views.Vehiculo import VehiculoCreate, VehiculoDelete, VehiculoUpdate, VehiculoDetailView, VehiculoListView
from vehiculos.views.Marca import MarcaCreate, MarcaUpdate, MarcaDelete, MarcaDetailView, MarcaListView
from vehiculos.views.Institucion import InstitucionCreate, InstitucionUpdate, InstitucionDelete, InstitucionDetailView, InstitucionListView
from django.contrib.auth.decorators import login_required
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

login_url='/inicio'

urlpatterns = patterns('',
    url(r'^inicio$', 'vehiculos.views.Usuarios.inicio', name='inicio'),
    url(r'^$', login_required(VehiculoListView.as_view(), login_url='/inicio'), name='vehiculos_registrados'),
    # vehiculo crud
    url(r'^vehiculos_registrados/$', login_required(VehiculoListView.as_view(), login_url), name='vehiculos_registrados'),
    url(r'^vehiculo/(?P<pk>\d+)/detalles/$', login_required(VehiculoDetailView.as_view(), login_url), name='vehiculo_detalles'),
    url(r'vehiculo/agregar/$', login_required(VehiculoCreate.as_view(), login_url), name='vehiculo_guardar'),
    url(r'vehiculo/(?P<pk>\d+)/$', login_required(VehiculoUpdate.as_view(), login_url), name='vehiculo_modificar'),
    url(r'vehiculo/(?P<pk>\d+)/eliminar/$', login_required(VehiculoDelete.as_view(), login_url), name='vehiculo_eliminar'),
    #marca crud
    url(r'^marcas_registradas/$', login_required(MarcaListView.as_view(), login_url), name='marcas_registradas'),
    url(r'^marca/(?P<pk>\d+)/detalles/$', login_required(MarcaDetailView.as_view(), login_url), name='marca_detalles'),
    url(r'marca/agregar/$', login_required(MarcaCreate.as_view(), login_url), name='marca_guardar'),
    url(r'marca/(?P<pk>\d+)/$', login_required(MarcaUpdate.as_view(), login_url), name='marca_modificar'),
    url(r'marca/(?P<pk>\d+)/eliminar/$', login_required(MarcaDelete.as_view(), login_url), name='marca_eliminar'),
    #institucion crud
    url(r'^instituciones_registradas/$', login_required(InstitucionListView.as_view(), login_url), name='instituciones_registradas'),
    url(r'^institucion/(?P<pk>\d+)/detalles/$', login_required(InstitucionDetailView.as_view(), login_url), name='institucion_detalles'),
    url(r'institucion/agregar/$', login_required(InstitucionCreate.as_view(), login_url), name='institucion_guardar'),
    url(r'institucion/(?P<pk>\d+)/$', login_required(InstitucionUpdate.as_view(), login_url), name='institucion_modificar'),
    url(r'institucion/(?P<pk>\d+)/eliminar/$', login_required(InstitucionDelete.as_view(), login_url), name='institucion_eliminar'),
    #usuario del sistema
    url(r'^cerrar/$', 'vehiculos.views.Usuarios.cerrar_sesion', name="cerrar_sesion"),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
    ),
)
