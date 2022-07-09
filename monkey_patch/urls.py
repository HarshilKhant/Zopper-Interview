from django.conf.urls import include, url
from monkey_patch.views import get_user_details

urlpatterns = [
    url(r'^admin/', admin.site.urls)]