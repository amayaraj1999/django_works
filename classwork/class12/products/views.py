from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny
from .forms import ProductForm
from .models import Product



@api_view(['POST'])
@permission_classes((AllowAny,))
def add_product(request):
    form = ProductForm(data=request.data)
    if form.is_valid():
        product = form.save()
        return Response(
            {
                "message": "Product added successfully",
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": str(product.price),
                    "category": product.category
                }
            },
            status=status.HTTP_201_CREATED
        )
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_products(request):
    products = Product.objects.all().values("id", "name", "price", "category")
    return Response(list(products), status=status.HTTP_200_OK)
