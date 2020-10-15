from django.urls import path
#from .views import morceau_detail
from .views import MorceauDetailView, MorceauList, MorceauCreate, MorceauDelete, MorceauUpdate
from .views import ArtisteDetailView, ArtisteList, ArtisteCreate, ArtisteDelete, ArtisteUpdate
app_name = 'musiques'

urlpatterns = [
    #path('<int:pk>', morceau_detail, name='morceau-detail')
    path('<int:pk>', MorceauDetailView.as_view(), name='morceau-detail'),
    path('', MorceauList.as_view(), name='morceau_list'),
    path('morceau', MorceauCreate.as_view(), name='morceau_create'),
    path('<int:pk>/delete/', MorceauDelete.as_view(), name='morceau-delete'),
    path('morceau/<int:pk>', MorceauUpdate.as_view(), name='morceau_update'),
    #path('<int:pk>', morceau_detail, name='morceau-detail')
    path('artiste/<int:pk>', ArtisteDetailView.as_view(), name='artiste-detail'),
    path('artiste', ArtisteList.as_view(), name='artiste_list'),
    path('artiste/new', ArtisteCreate.as_view(), name='artiste_create'),
    path('artiste/<int:pk>/delete/', ArtisteDelete.as_view(), name='artiste-delete'),
    path('artiste/<int:pk>/update', ArtisteUpdate.as_view(), name='artiste_update'),
 ]
