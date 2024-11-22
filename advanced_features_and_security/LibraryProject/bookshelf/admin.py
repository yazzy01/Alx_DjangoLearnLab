from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the admin list view
    search_fields = ('title', 'author')                      # Fields to search in the admin
    list_filter = ('publication_year',)                      # Add filters for publication year



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)  # Register the Book model if it's not already registered


from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Book

# Add groups and permissions in the Django Admin interface
admin.site.site_header = 'My Admin Panel'

# Create custom permissions in the admin site
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_year']

    def save_model(self, request, obj, form, change):
        # Add logic to assign custom permissions
        super().save_model(request, obj, form, change)
        book_permissions = obj._meta.permissions
        for permission in book_permissions:
            group = Group.objects.get(name='Editors')
            group.permissions.add(permission)

admin.site.register(Book, BookAdmin)

