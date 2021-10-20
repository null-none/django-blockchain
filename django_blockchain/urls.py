from django.conf.urls import url, include

urlpatterns = [
    url(r"^api/v1/", include("chain.api.v1.urls"), name="api"),
]
