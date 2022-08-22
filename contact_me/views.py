from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact, Replay
from .serializers import ContactSerializer, ReplaySerializer


class ContactList(APIView):
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


class ContactDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        """
        :param pk:
        :return:
        """
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        :param request:
        :param pk:
        :param format:
        :return:
        """
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        context = {
            "status": True,
            "message": "Get Contact Data",
            "data": serializer.data,
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """
        :param request:
        :param pk:
        :param format:
        :return:
        """
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "status": True,
                "message": "Contact successfully updated !",
                "data": serializer.data
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """

        :param request:
        :param pk:
        :param format:
        :return:
        """
        contact = self.get_object(pk)
        contact.delete()
        context = {
            "status": True,
            "message": "Contact successfully Deleted !",
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)
