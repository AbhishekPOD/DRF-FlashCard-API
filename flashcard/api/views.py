
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Card
from .serializers import CardSerializer
 
@api_view(['GET'])
def index(request):
    api_urls = {
        'Show all cards': 'GET /cards',
        'Create a new card': 'POST /cards',
        'Search a card by id': 'GET /card/<id>',
        'Update a card (full update)': 'PUT /card/<id>',
        'Update a card (partial update)': 'PATCH /card/<id>',
        'Delete a card': 'DELETE /card/<id>'
    }
 
    return Response(api_urls)

class CardList(APIView):
    def get(self, request):
        cards = Card.objects.all()
        # print(cards)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CardDetail(APIView):
    def get_object(self, id):
        try:
            return Card.objects.get(id=id)
        except Card.DoesNotExist:
            return None

    def get(self, request, id):
        card = self.get_object(id)
        # print(card)
        if card:
            serializer = CardSerializer(card)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        card = self.get_object(id)
        if card:
            serializer = CardSerializer(card, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        card = self.get_object(id)
        # print(card)
        if card:
            serializer = CardSerializer(card, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        card = self.get_object(id)
        if card:
            card.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)