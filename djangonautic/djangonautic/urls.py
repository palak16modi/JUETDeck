from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^about/$',views.about), # ^ means start $ means end... so it will search for /about
    url(r'^home/$',article_views.article_list, name = 'home'),
    url(r'^blog/$',article_views.article_list, name = 'home'),#this will look for home page like .com no forward slash nothing
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
