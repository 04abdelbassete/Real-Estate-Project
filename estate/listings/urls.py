from django.urls import path, include

from .views import (estates_list, estate_view, create_house, create_plot_of_land, update,
                     search, dashboard, delete, payment, payment_success, payment_failed)

urlpatterns = [
    path("", estates_list, name="estates_list"),
    path("estate/<slug:slug>", estate_view, name="estate_view"),
    path("estates/houses/create", create_house, name="create_house"),
    path("estates/plots-of-land/create", create_plot_of_land, name="create_plot_of_land"),
    path("estates/update/<slug:slug>", update, name="update"),
    path("estates/delete", delete, name="delete"),
    path("estates/dashboard", dashboard, name="dashboard"),
    path("estates/search/<slug:srch>", search, name="search"),
    path("estates/payment/", payment, name="payment"),
    path("paypal", include('paypal.standard.ipn.urls')),
    path("estates/payment/payment-success", payment_success, name="payment_success"),
    path("estates/payment/payment-failed", payment_failed, name="payment_failed"),
]
