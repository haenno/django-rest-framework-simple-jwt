# django-rest-framework-simple-jwt
Absolute bare minimum with Django REST framework and Simple JWT and all settings to default/standard.

Espacially for usage with my frontend project: <https://github.com/haenno/VBJ>

## Usage

```bash
git clone *this repo*
conda create --name drfjwt python=3.10 # or use your existing environment
pip install -r requirements.txt
cd drfjwt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open <http://127.0.0.1:8000/> in your browser and login with the superuser credentials. Usefull for testing is also:

- The Djnago Admin interface: <http://127.0.0.1:8000/admin>
- Any mistyped URL, as it will show you the available URLs :-)

## Installation and setup log

```bash
conda create --name drfjwt python=3.10
conda activate drfjwt
pip install Django djangorestframework djangorestframework-simplejwt
pip freeze > requirements.txt
django-admin startproject drfjwt
cd drfjwt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```


Add to ``settings.py`` in ``INSTALLED_APPS``: 

```python
    'rest_framework',
    'rest_framework_simplejwt',
```

Then add also to ``settings.py`` at the end:

```python
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],    
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

Then add to ``urls.py`` in ``urlpatterns``:

```python
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
```

Then add to ``urls.py`` between ``urlpatterns`` and the imports:

```python
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "username",
            "email",
            "is_staff",
            "is_active",
            "is_superuser",
            "password",
            "first_name",
            "last_name",
        ]


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
```
