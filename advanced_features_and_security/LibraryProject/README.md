# Permissions Setup

## Custom Permissions
- `can_view`: View access to the Book model
- `can_create`: Create access to the Book model
- `can_edit`: Edit access to the Book model
- `can_delete`: Delete access to the Book model

## Groups
- `Viewers`: Can only view books (`can_view`)
- `Editors`: Can view, create, and edit books (`can_view`, `can_create`, `can_edit`)
- `Admins`: Can view, create, edit, and delete books (`can_view`, `can_create`, `can_edit`, `can_delete`)

## Example Usage
To enforce permissions in views, use the `@permission_required` decorator:
```python
@permission_required('books.can_edit', raise_exception=True)
def edit_book(request, book_id):
    ...

