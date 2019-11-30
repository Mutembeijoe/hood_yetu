from django.urls import path
from .views import NeighbourhoodDetailView, NeighbourhoodListView, join_neighbourhood, leave_neighbourhood

urlpatterns = [
    path('<int:pk>/',NeighbourhoodDetailView.as_view(),name='neighbourhood'),
    path('all/', NeighbourhoodListView.as_view(), name='neighbourhood_list' ),
    path('join/<int:community_id>/',join_neighbourhood, name='join_neighbourhood' ),
    path('leave/<int:community_id>/',leave_neighbourhood, name='leave_neighbourhood' ),
]