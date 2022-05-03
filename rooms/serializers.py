from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Room


class RoomSerializer(serializers.ModelSerializer):

    """Python to JSON object"""

    user = UserSerializer()

    class Meta:
        model = Room
        exclude = ("modified",)
