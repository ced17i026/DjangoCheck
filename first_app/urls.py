from django.urls import path
from first_app import views
urlpatterns = [
    path('',views.index,name="index"),
    path('form',views.form_page,name="form"),
    path('help/',views.help,name="help"),
    path('sign_up',views.sign_up,name="sign_up"),
]