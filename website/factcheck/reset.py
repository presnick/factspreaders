from django.contrib.auth.models import User
user = User.objects.all()[0]
user.set_password('admin')
user.save()
