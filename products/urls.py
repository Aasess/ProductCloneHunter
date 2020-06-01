from django.urls import path
#from . import views
from products import views

urlpatterns = [
    path("",views.home,name="home"),
    path("create/",views.create,name ="create"),
    path("<int:product_id>/",views.details,name="details"),
    path("<int:product_id>/upvote",views.upvote,name="upvote"),
    path("<int:product_id>/upvotehome",views.upvotehome,name="upvotehome")
]