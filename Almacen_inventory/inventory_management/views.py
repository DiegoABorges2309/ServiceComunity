from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ItemSerializer
from .models import Items

class ItemGeneral(APIView):
    #Add new Item
    def post(self, request):
        _serializer = ItemSerializer(data=request.data)
        if _serializer.is_valid():
            _serializer.save()
            return Response(status= 201)
        else:
            return Response(status=400)

    #get All Items
    def get(self, request):
        try :
            _items = Items.objects.all()
            _items_serializer = ItemSerializer(_items, many=True)
            return Response(_items_serializer.data, status= 200)
        except Exception as e:
            return Response(status=404)

class ItemSpecific(APIView):
    #Get one item
    def get(self, request, name_item):
        try :
            _items = Items.objects.filter(name_item__icontains=name_item)
            _items_serializer = ItemSerializer(_items, many=True)
            return Response(_items_serializer.data, status=200)
        except Exception as e :
            return Response(status=404)

    #Update item info
    def put(self, request, name_item):
        try :
            _item_model = Items.objects.get(name_item = name_item)
            _item_serializer = ItemSerializer(_item_model, data = request.data)
            if _item_serializer.is_valid():
                _item_serializer.save()
                return Response(status= 200)
            else :
                return Response(status= 400)
        except Exception as e:
            print(f"ERROR: {e}")
            return Response(status=404)

    #Delete Item
    def delete(self, request, name_item):
        try :
            _item_model = Items.objects.get(name_item = name_item)
            _item_model.delete()
            return Response(status=200)
        except Exception as e:
            return Response(status=404)