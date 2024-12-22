from rest_framework.views import APIView
from .models import ExelNameItem
from .serializer import ExelNameItemSerializer
from rest_framework.response import Response

class AddExelName(APIView):
    def pos(self, request):
        try :
            _serializer = ExelNameItemSerializer(data=request.data, many= True)
            if _serializer.is_valid():
                _serializer.save()
                return Response(status=200)
            else:
                raise ValueError
        except ValueError as e:
            return Response(status=400)