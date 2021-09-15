from import_export import resources
from .models import sci1
from django.contrib.auth.models import User

class resourcessci1(resources.ModelResource):
    class meta:
        model = sci1

class reuser(resources.ModelResource):
    class meta:
        model = User
