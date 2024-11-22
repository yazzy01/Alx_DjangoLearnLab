from django.contrib import admin
from django.urls import path
from relationship_app import views  # Import views from the app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.book_list, name='book_list'),
    path('libraries/', views.library_list, name='library_list'),
    path('librarians/', views.librarian_list, name='librarian_list'),
    path('bookshelf/', include('bookshelf.urls')),
]

