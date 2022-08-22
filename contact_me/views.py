from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact, Replay
from .serializers import ContactSerializer, ReplaySerializer


class ContactAPIView(APIView):
    """
    List all Contact, or create a new Contact.
    """

    def get(self, request, format=None):
        try:
            contact = Contact.objects.all()
            serializer = ContactSerializer(contact, many=True)
            context = {
                "status": True,
                "message": "Get Contact Data",
                "data": serializer.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        except Contact.DoesNotExist:
            context = {
                "Status": False,
                "Message": "No Data Found !",
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "status": True,
                "message": "Contact successfully created !",
                "data": serializer.data
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
