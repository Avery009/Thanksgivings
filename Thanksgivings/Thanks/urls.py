from django.urls import path

from . import views

urlpatterns = [
	path('', views.thanksgivings, name = 'Prayers'),
	path('thanksgiving/', views.thanksgiving, name = 'Prayer Request'),
	path('thanks/<int:prayer_id>/', views.thanks, name = 'Prayer'),
	path('givethanks/<int:prayer_id>', views.givethanks, name = 'Prayers'),
	path('increasethanks/<int:prayer_id>/<int:prayer_count>', views.increasethanks, name = "Pray"),
]
