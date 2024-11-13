from django.urls import path
from .views import list_books
from .views import LibraryDetailView  # Ensure both views are imported

urlpatterns = [
    # URL for class-based view to show library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # URL for function-based view to list books
    path('books/', list_books, name='list_books'),
]



from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]

