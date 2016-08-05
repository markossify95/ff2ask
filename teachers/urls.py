from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# instapool.io/teachers/
urlpatterns = [
    url(r'^all/$', view=views.TeacherList.as_view(), name='all-teachers'),
    url(r'^(?P<pk>[0-9]+)/$', views.TeacherInstance.as_view(), name='teacher-instance'),
    url(r'^(?P<fk>[0-9]+)/questions/$', views.QuestionList.as_view(), name='t-questions'),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionInstance.as_view(), name='t-question-instance'),
    url(r'^questions/(?P<fk>[0-9]+)/answers/$', views.AnswerList.as_view(), name='t-question-answers'),
    url(r'^questions/(?P<fk>[0-9]+)/answers/(?P<pk>[0-9]+)/$', views.AnswerInstance.as_view(),
        name='t-answer-instance'),
    url(r'questions/(?P<fk>[0-9]+)/answers/(?P<pk>[0-9]+)/vote/$', views.Voter.as_view(), name='t-answer-voter'),
]
