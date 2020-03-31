from django.contrib import admin
from django.urls import path

from django_test.api import views as api_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('apps/', api_views.AppListCreateView.as_view(), name='app-list-create'),
    path('apps/<int:id>', api_views.AppRetrieveView.as_view(), name='app-list-retrieve'),
    path('api/test', api_views.AppKeyRetrieveView.as_view(), name='app-key-retrieve-view'),
    path('apps/reset_key/', api_views.AppResetKeyView.as_view(), name='app-reset-key-view')
]
