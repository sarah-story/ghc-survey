from django.conf.urls import patterns, include, url
import questions

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'survey.views.home', name='home'),
    # url(r'^survey/', include('survey.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^survey/$', 'questions.views.index', name='index'),
    url(r'^survey/2/(?P<person>.+)/$', 'questions.views.page_two', name='page_two'),
)
