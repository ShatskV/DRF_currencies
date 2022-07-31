from django.urls import include, path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('login/', views.CustomAuthToken.as_view()),
    path('currencies/', views.CurrencyViewSet.as_view({'get': 'list'})),
    path('currency/<int:pk>', views.CurrencyViewSet.as_view({'get': 'retrieve'})),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

