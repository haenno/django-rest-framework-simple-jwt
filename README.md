# django-rest-framework-simple-jwt
Absolute bare minimum with Django REST framework and Simple JWT and all settings to default/standard.

Espacially for usage with my frontend project: <https://github.com/haenno/VBJ>

## API endpoints for JWT authentication

- Obtain a token pair for a user: POST to ``/api/token/`` with ``username, password``
- Verify a token: POST to ``/api/token/verify/`` with ``token``  *(works on both access and refresh tokens)*
- Refresh a token: POST to ``/api/token/refresh/`` with ``refresh`` *(refresh token only, returns fresh access and refresh tokens)*
- Blacklist a token: POST to ``/api/token/blacklist/`` with ``refresh`` *(blacklists any kind of token, refresh or access)*

## Usage

```bash
git clone *this repo*
conda create --name drfjwt python=3.10 # or use your existing environment
pip install -r requirements.txt
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
pip install Django djangorestframework djangorestframework-simplejwt django-cors-headers
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
    'rest_framework_simplejwt.token_blacklist',    
    'corsheaders',
```

Add to ``settings.py`` in ``MIDDLEWARE``:

```python
    'corsheaders.middleware.CorsMiddleware',
```

Then add also to ``settings.py`` at the start:

```python
from datetime import timedelta
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

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

CORS_ORIGIN_ALLOW_ALL = True

```

Then add to ``urls.py`` in ``urlpatterns``:

```python
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist',
    ),    
```

Then add to ``urls.py`` between ``urlpatterns`` and the imports:

```python
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
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
