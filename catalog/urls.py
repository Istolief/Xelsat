from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^brand/(?P<brand>[-\w]+)/$', views.product_list, name='product_list'),
    url(r'^category/(?P<category>[-\w]+)/$', views.product_list, name='product_list'),
    url(r'^category/(?P<category>[-\w]+)/(?P<brand>[-\w]+)/$', views.product_list, name='product_list'),
    url(r'^top_category/(?P<top_category>[-\w]+)/$', views.product_list, name='product_list'),
    url(r'^top_category/(?P<top_category>[-\w]+)/(?P<brand>[-\w]+)/$', views.product_list, name='product_list'),

]
