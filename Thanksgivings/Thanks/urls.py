from django.urls import path

from . import views

app_name="Thanks"
urlpatterns = [
	path('', views.thanksgivings, name = 'Thanks_Givings'),
	path('thanksgiving/', views.thanksgiving, name = 'Thanksgiving'),
	path('thanks/<int:thanks_id>/', views.thanks, name = 'Thanksgiving'),
	path('givethanks/<int:thanks_id>', views.givethanks, name = 'Give_Thanks'),
	path('increasethanks/<int:thanks_id>/<int:givethanks_count>', views.increasethanks, name = "Increase_Thanks"),
]
