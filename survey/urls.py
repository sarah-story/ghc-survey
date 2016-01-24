from django.conf.urls import patterns, include, url
from django.contrib import admin
import questions

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'survey.views.home', name='home'),
    # url(r'^survey/', include('survey.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^survey/$', 'questions.views.index', name='index'),
    url(r'^survey/2', 'questions.views.page_two', name='page_two'),
    url(r'^survey/done', 'questions.views.done', name='done'),
    url(r'^survey/3', 'questions.views.page_three', name='page_three'),
    url(r'^survey/contact', 'questions.views.contact', name='contact'),
    url(r'^survey/complete', 'questions.views.success', name="success")
)
