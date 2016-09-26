from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

# https://www.instapool.io/audience/
app_name = 'audience'
urlpatterns = [
    url(r'^questions/all/$', views.AudienceQuestionList.as_view(), name='all-audience-questions'),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.AQInstance.as_view(), name='aq-instance'),
    url(r'^questions/vote/$', views.Voter.as_view(), name='aq-list'),
    url(r'^questions/vote/(?P<pk>[0-9]+)/$', views.Voter.as_view(), name='aq-voter'),
    url(r'^questions/new/$', views.NewAudienceQuestion.as_view(), name='new-aq'),
]
