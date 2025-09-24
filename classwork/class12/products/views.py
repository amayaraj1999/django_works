from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny

# Temporary product list (in-memory, not database)
products = []

@api_view(['POST'])
@permission_classes((AllowAny,))
def add_product(request):
    
    name = request.data.get("name")
    price = request.data.get("price")
    category = request.data.get("category")

    if not name or not price or not category:
        return Response({"error": "All fields are required (name, price, category)"},
                        status=status.HTTP_400_BAD_REQUEST)

    product = {"name": name, "price": price, "category": category}
    products.append(product)

    return Response({"message": "Product added successfully", "product": product},
                    status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_products(request):
    """Returns all products"""
    return Response(products, status=status.HTTP_200_OK)
