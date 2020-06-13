from django.urls import path
from .  import views


urlpatterns = [
	path('Factory-Revenue/',views.factory_revenue_view,name='factory_view'),
	path('Operation-Report/',views.operation_view,name='operation_view'),
	path('Hydro-Report/',views.hydro_view,name='hydro_view'),
	path('Summary-Report/',views.summary_view,name='summary_view'),
	path('Operation-Import/',views.operation_import_view,name='operation_import_view'),
]