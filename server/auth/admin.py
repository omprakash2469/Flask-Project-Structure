from ..extensions import admin, db
from .models import User
from .views import UsersView

# Register your views here
admin.add_view(UsersView(User, db.session))