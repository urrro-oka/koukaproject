from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('signup_success/',views.SignUpSuccessView.as_view(),name='signup_success'),
    path('login/',auth_view.LoginView.as_view(template_name = 'login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name = 'logout.html'),name='logout'),
]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)