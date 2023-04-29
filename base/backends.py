from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class MongoDBAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()

        try:
            # Retrieve the user from MongoDB based on the username
            user = User.objects.get(username=username)

            # Check if the password matches
            if user.check_password(password):
                print(user)
                return user
        except User.DoesNotExist:
            return None

        return None
