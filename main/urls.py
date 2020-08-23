from django.urls import path
from .views import index
from .views import other_page
from .views import JobLoginView
from .views import profile
from .views import JobLogoutView
from .views import ChangeUserInfoView
from .views import JobPasswordChangeView
from .views import RegisterUserView, RegisterDoneView
from .views import user_activate
from .views import DeleteUserView

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('<str:page>/', other_page, name='other'),
    path('accounts/login/', JobLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', JobLogoutView.as_view(), name='logout'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('acoounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', JobPasswordChangeView.as_view(), name='password_change'),
    path('acoounts/register/done/', RegisterDoneView.as_view(), name="register_done"),
    path('acoounts/register/', RegisterUserView.as_view(), name="register"),
    path('acoounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    ]