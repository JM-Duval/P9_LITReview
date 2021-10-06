from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('review/', views.review, name='review'),
	path('review/<int:ticket_id>/', views.review, name='review'),
	path('modifyreview/<int:review_id>', views.modify_review, name='modifyreview'),
	path('deletereview/<int:review_id>', views.delete_review, name='deletereview'),
	path('modifyticketinreview/<int:ticket_id>/', views.modify_ticket_in_review, 
		name='modifyticketinreview')
]
