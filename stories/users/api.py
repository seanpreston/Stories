from django.contrib.auth.models import User

from rest_framework import response
from rest_framework import status
from rest_framework import views


class UserView(views.APIView):

    def post(self, request, *args, **kwargs):
        access_token = request.data.get('access_token')
        user_id = request.data.get('user_id')

        User.objects.get_or_create(
            profile__facebook_access_token=access_token,
            profile__facebook_id=user_id,
        )

        return response.Response(status=status.HTTP_200_OK)
