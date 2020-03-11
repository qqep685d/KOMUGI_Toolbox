from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('findocs/',  include('FinDocs.urls')),
    path('accounts/', include('Accounts.urls')),
    path('admin/', admin.site.urls),
]
