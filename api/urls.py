from django.conf.urls import url, include
from . import views

urlpatterns = [ 
    url(r'^locations/$', views.LocationList.as_view(), name='location_list'),
    url(r'^locations/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view(), name='location_detail'),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns += [
        url(r'^auth/', include('rest_framework.urls',
                                    namespace='rest_framework')),
]