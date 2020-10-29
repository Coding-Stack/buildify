from django.urls import path
from django.conf.urls import url

from . import views as v

urlpatterns = [
    path('', v.index,name='index'),
    path('login',v.login,name='login'),
    path('signup',v.signup,name='signup'),
    path('home',v.home,name='home'),
    path('register',v.register,name='register'),
    path('signin',v.signin,name='signin'),
    path('logout',v.logout,name='logout'),
    path('plan/new', v.new_plan, name='new_plan'),
    path('get_plan/<status>',v.get_plan,name='get_plan'),
    path('update_plan/<int:id>',v.update_plan,name='update_plan'),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)