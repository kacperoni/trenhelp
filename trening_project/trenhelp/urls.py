from django.urls import path
from trenhelp.views import (TrenhelpDetailView,TrenhelpCreateView,TrenhelpDeleteView,
                            TrenhelpUpdateView,TrenhelpExerciseUpdateView,TrenhelpExerciseCreateView,
                            TrenhelpExerciseDeleteView, create_training)
app_name = 'trenhelp'

urlpatterns = [
    path('training/<int:pk>/',TrenhelpDetailView.as_view(),name='trenhelp_detail'),
    path('training/add/',create_training,name='trenhelp_add'),
    path('training/delete/<int:pk>',TrenhelpDeleteView.as_view(), name='trenhelp_delete'),
    path('training/update/<int:pk>',TrenhelpUpdateView.as_view(), name='trenhelp_update'),
    path('training/exercise/update/<int:pk>',TrenhelpExerciseUpdateView.as_view(),name='exercise_update'),
    path('training/<int:pk>/exercise/add',TrenhelpExerciseCreateView.as_view(),name='exercise_create'),
    path('training/exercise/delete/<int:pk>',TrenhelpExerciseDeleteView.as_view(),name='exercise_delete'),
]