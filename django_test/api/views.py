from django import shortcuts
from django.core import exceptions
from rest_framework import generics, response, permissions, status, views

from . import models, serializers


class AppListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.AppSerializer
    permission_classes = [permissions.AllowAny]

    queryset = models.App.objects.all()


class AppRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AppSerializer
    permission_classes = [permissions.AllowAny]

    queryset = models.App.objects.all()
    lookup_field = 'id'


class AppKeyRetrieveView(generics.RetrieveAPIView):
    serializer_class = serializers.AppSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        api_key = self.request.query_params.get('api_key')
        if not api_key:
            raise exceptions.PermissionDenied()

        app = models.App.objects.filter(api_key=api_key).first()
        if not app:
            raise exceptions.PermissionDenied()

        return app


class AppResetKeyView(views.APIView):
    def post(self, request, format=None):
        app_id = request.data.get('app_id')
        if not app_id:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

        app = shortcuts.get_object_or_404(models.App, id=app_id)
        app.api_key = models.generate_api_key()
        app.save()

        return response.Response(status=status.HTTP_200_OK)
