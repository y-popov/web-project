from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', 'qa.views.new_questions', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'qa.views.test', name='login'),
    url(r'^signup/', 'qa.views.test', name='signup'),
    url(r'^question/(?P<id>.+)/$', 'qa.views.question_page', name='quest'),
    url(r'^ask/', 'qa.views.test', name='ask'),
    url(r'^popular/', 'qa.views.popular', name='pop'),
    url(r'^new/', 'qa.views.test', name='new')
]
