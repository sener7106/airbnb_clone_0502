from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer

# generic view 는 페이지의 정보를 담은 view


@api_view(["GET", "POST"])
def rooms_view(request):
    if request.method == "GET":
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True).data
        return Response(serializer)
    elif request.method == "POST":
        pass


class SeeRoomView(RetrieveAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
