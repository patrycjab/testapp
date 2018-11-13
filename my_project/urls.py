from django.conf.urls import url
from django.contrib import admin
from email_app.views import ViewEmailSend

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ViewEmailSend.as_view()),
]
