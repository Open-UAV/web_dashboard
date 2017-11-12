from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [



                  #Page URLs
    url(r'^$', views.index, name='label_index'),
    url(r'^label$', views.label, name='label'),
    url(r'^simulate$', views.simulate, name='simulate'),
    url(r'^console$', views.console, name='console'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^dev_console$', views.dev_console, name='dev_console'),
    url(r'^hook$', views.hook, name='hook'),
    url(r'^dev_hook$', views.dev_hook, name='dev_hook'),


    #GET/POST URLs

    #url(r'^purge$', 'webclient.views.purge'),
    url(r'^getInfo$', 'webclient.views.getInfo'),
    url(r'^applyLabels$', 'webclient.views.applyLabels'),
    url(r'^loadLabels$', 'webclient.views.loadLabels'),


    url(r'^get_overlayed_image/(?P<image_label_id>[0-9]*)$', 'webclient.views.get_overlayed_image'),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
