from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# https://www.instapool.io/audience/
urlpatterns = [
    url(r'^questions/all/$', views.AudienceQuestionList.as_view(), name='all-audience-questions'),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.AQInstance.as_view(), name='aq-instance'),
    url(r'^questions/(?P<pk>[0-9]+)/vote/$', views.Voter.as_view(), name='aq-voter'),
]
