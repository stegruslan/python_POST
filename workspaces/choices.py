from django.db.models import Choices


class RoleChoice(Choices):
    ADMIN = 'admin'
    MEMBER = 'member'
    OWNER = 'owner'
