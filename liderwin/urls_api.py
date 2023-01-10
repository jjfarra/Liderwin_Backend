from django.urls import path, include

urlpatterns = [
    path('management/', include('management.urls')),
]

urlpatterns = [path("api/", include(urlpatterns))]