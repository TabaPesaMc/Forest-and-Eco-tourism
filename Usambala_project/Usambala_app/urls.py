from django.urls import path,include
from .import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('donate',views.donate,name='donate'),
    path('gallery',views.gallery,name='gallery'),
    path('project',views.project,name='project'),
    # path('',views.home,name='home'),

]