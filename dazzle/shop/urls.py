
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("productview/", views.productview, name="ProductView"),
    path("tracker/", views.tracker, name="TrackerStatus"),
    path("search/", views.search, name="Search"),
    path("checkout/", views.checkout, name="CheckOut"),
]