from django.conf.urls import patterns, include, url
from pmi.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProjectAdmin.views.Proyecto', name='proyecto'),
    # url(r'^blog/', include('blog.urls')),
  

    url(r'^admin/', include(admin.site.urls)),
    url(r'^Editar_proyecto/informacion_tareas/agregar_tarea/$', crearTarea),
    url(r'^proyectos/$', proyectos),
    url(r'^Editar_proyecto/informacion_proyecto/$', informacionDeProyecto),
    url(r'^crear_proyecto/$', crearProyecto),
    url(r'^Editar_proyecto/informacion_tareas/$', informeTareas),

    
)
