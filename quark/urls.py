from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('docs.urls')),
    path('blog/', include('blog.urls')),
    path('pcra/', include('atom.urls')),
]
