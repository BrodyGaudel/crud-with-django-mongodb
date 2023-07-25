# myapp/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Produit
from .serializers import ProduitSerializer


@api_view(['GET'])
def getAllProduct(request):
    produits = Produit.objects.all()
    serializer = ProduitSerializer(produits, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getProductById(request, id):
    try:
        produit = Produit.objects.get(id=id)
        serializer = ProduitSerializer(produit)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Produit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def saveProduct(request):
    serializer = ProduitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteProductById(request, id):
    try:
        produit = Produit.objects.get(id=id)
        produit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Produit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def updateProduct(request, id):
    try:
        produit = Produit.objects.get(id=id)
        serializer = ProduitSerializer(produit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Produit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)