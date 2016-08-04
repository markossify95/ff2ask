from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# instapool.io/teachers/
urlpatterns = [
    url(r'^all/$', view=views.TeacherList.as_view(), name='all-teachers'),
    url(r'^(?P<pk>[0-9]+)/$', views.TeacherInstance.as_view(), name='teacher-instance'),
    url(r'^(?P<fk>[0-9]+)/questions/$', views.QuestionList.as_view(), name='questions-by-teacher'),
]
