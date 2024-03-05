from django.urls import path
from .views import home_views,login_views,signup_views,scrapbook_views,timecapsule_views,maps_views,albums_views,layout1_views,layout2_views
urlpatterns=[path('', home_views, name='home'),
             path('login/', login_views, name='login'),
             path('signup/', signup_views, name='signup'),
             path('scrapbook/', scrapbook_views, name='scrapbook'),
             path('timecapsule/', timecapsule_views, name='timecapsule'),
             path('maps/', maps_views, name='maps'),
             path('albums/', albums_views, name='albums'),
             path('scrapbook/layout1/', layout1_views, name='layout1'),
             path('scrapbook/template1/', layout2_views, name='template1'),]