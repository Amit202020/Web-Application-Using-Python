

from django.conf.urls import url
from users.views import dashboard


urlpatterns = [
        url("dashboard/",dashboard,name="dashboard")
]
