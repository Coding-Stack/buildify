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
    path('new_construction/<int:id>',v.new_construction,name='new_construction'),
    path('update_construction/<int:id>',v.update_construction,name='update_construction'),
    path('get_construction/<status>',v.get_construction,name='get_construction'),
    path('get_worker',v.get_worker,name='get_worker'),
    path('update_worker/<int:id>',v.update_worker,name='update_worker'),
    path('get_const_worker/<int:id>',v.get_const_worker,name='get_const_worker'),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)