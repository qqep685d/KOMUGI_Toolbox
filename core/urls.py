from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/home', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('FinDocs.urls')),
]
