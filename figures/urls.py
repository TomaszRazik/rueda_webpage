from django.urls import path, include, re_path
from figures import views

app_name='figures'

urlpatterns = [
    path(r'^tables/', views.TablesView, name='tables'),
    path(r'^create_word/', views.DictionaryCreateView.as_view(), name='create_word'),
    path(r'^update_word/(?P<pk>[-\w]+)/$', views.DictionaryUpdateView.as_view(), name='update_word'),
    path(r'^delete_word/(?P<pk>[-\w]+)/$', views.DictionaryDeleteView.as_view(), name='delete_word'),
    path(r'^create_figure/', views.FiguresCreateView.as_view(), name= 'create_figure'),
    path(r'^update_figure/(?P<pk>[-\w]+)/$', views.FiguresUpdateView.as_view(), name='update_figure'),
    path(r'^delete_figure/(?P<pk>[-\w]+)/$', views.FiguresDeleteView.as_view(), name='delete_figure'),


]
