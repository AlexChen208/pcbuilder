from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cases/', views.cases_index, name='index'),
    path('cases/<int:case_id>/',views.cases_detail,name='detail'),
    path('account/signup/', views.signup, name='signup'),
    path('cases/create/', views.CaseCreate.as_view(), name='cases_create'),
    path('cases/<int:pk>/update/', views.CaseUpdate.as_view(), name='cases_update'),
    path('cases/<int:pk>/delete/', views.CaseDelete.as_view(), name='cases_delete'),
    path('cases/<int:case_id>/add_comment/', views.add_comment, name='add_comment'),
    path('components/', views.ComponentList.as_view(), name='components_index'),
    path('components/<int:pk>/', views.ComponentDetail.as_view(), name='components_detail'),
    path('components/create/', views.ComponentCreate.as_view(), name='components_create'),
    path('components/<int:pk>/update/', views.ComponentUpdate.as_view(), name='components_update'),
    path('components/<int:pk>/delete/', views.ComponentDelete.as_view(), name='components_delete'),
    path('cases/<int:case_id>/assoc_component/<int:component_id>/', views.assoc_component, name='assoc_component'),
    path('cases/<int:case_id>/unassoc_component/<int:component_id>/', views.unassoc_component, name='unassoc_component'),
    path('cases/<int:case_id>/add_photo/', views.add_photo, name='add_photo')
]