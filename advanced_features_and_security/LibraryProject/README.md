# Custom Permissions and Groups Setup

## Custom Permissions (on Book model)
- `can_view`: Can view books
- `can_create`: Can create new books
- `can_edit`: Can edit existing books
- `can_delete`: Can delete books

## User Groups
- **Viewers**: Assigned `can_view`
- **Editors**: Assigned `can_view`, `can_create`, `can_edit`
- **Admins**: Assigned all permissions

## How It Works
- Views are protected using `@permission_required` decorators.
- Users must belong to a group that has the correct permission to access a view.
- Permissions are checked at runtime, and unauthorized access raises `PermissionDenied`.

## Testing
Use Django admin to assign users to the groups above and test access to different views like:
- `/books/`
- `/books/create/`
- `/books/edit/<id>/`
- `/books/delete/<id>/`

