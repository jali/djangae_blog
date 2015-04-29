from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^entry/add/$', views.BlogAddEntry.as_view(), name="entry-new"),
    url(r'^entry/edit/$', views.BlogEditEntry.as_view(), name="entry-edit"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry-detail"),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    # url(r'^user/', include('djangae.contrib.gauth.urls')),
)