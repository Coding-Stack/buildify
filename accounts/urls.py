from django.urls import path
from django.conf.urls import url

from . import views as v

urlpatterns = [
    path('', v.index,name='index'),
    path('login',v.login,name='login'),
    path('signup',v.signup,name='signup'),
    path('contact',v.contact,name='contact'),
    path('about_us',v.about_us,name='about_us'),
    path('home',v.home,name='home'),
    path('register',v.register,name='register'),
    path('signin',v.signin,name='signin'),
    path('edit_profile',v.edit_profile,name='edit_profile'),
    path('logout',v.logout,name='logout'),
    path('plan/new', v.new_plan, name='new_plan'),
    path('get_plan/<status>',v.get_plan,name='get_plan'),
    path('get_adminplan/<status>',v.get_adminplan,name='get_adminplan'),
    path('get_adminacceptedplan',v.get_adminacceptedplan,name='get_adminacceptedplan'),
    path('update_plan/<int:id>',v.update_plan,name='update_plan'),
    path('update_client_plan/<int:id>',v.update_client_plan,name='update_client_plan'),
    path('new_construction/<int:id>',v.new_construction,name='new_construction'),
    path('update_construction/<int:id>',v.update_construction,name='update_construction'),
    path('get_s_construction/<int:id>',v.get_s_construction,name='get_s_construction'),
    path('get_construction/<status>',v.get_construction,name='get_construction'),
    path('get_adminconstruction/<status>',v.get_adminconstruction,name='get_adminconstruction'),
    path('get_worker',v.get_worker,name='get_worker'),
    path('update_worker/<int:id>',v.update_worker,name='update_worker'),
    path('get_const_worker/<int:id>',v.get_const_worker,name='get_const_worker'),
    path('new_material',v.new_material,name='new_material'),
    path('get_material',v.get_material,name='get_material'),
    path('update_material/<int:id>',v.update_material,name='update_material'),

    path('worker_form',v.worker_form,name='worker_form'),
    path('apply',v.apply,name='apply'),
    path('update_workerprofile/<int:id>',v.update_workerprofile,name='update_workerprofile'),
    path('get_bill/<int:id>',v.get_bill,name='get_bill'),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)