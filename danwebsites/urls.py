from django.conf.urls import patterns, include, url
from django.contrib import admin
from danwebsitesapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'danwebsites.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', views.events, name='events'),
    url(r'^$', views.index, name='index'),
    url(r'^testimonials/', views.testimonials, name='testimonials'),
    url(r'^contact/', views.contact, name='contact'),
)
