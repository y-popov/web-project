from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', 'ask.views.test', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'ask.views.test', name='login'),
    url(r'^signup/', 'ask.views.test', name='signup'),
    url(r'^question/.+/', 'ask.views.test'),
    url(r'^ask/', 'ask.views.test', name='ask'),
    url(r'^popular/', 'ask.views.test', name='pop'),
    url(r'^new/', 'ask.views.test', name='new')
]
