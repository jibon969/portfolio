from .models import Contact, Replay
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'subject',
            'name',
            'phone',
            'message',
        ]


class ReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Replay
        fields = [
            'id',
            'send_to',
            'subject',
            'message',
        ]
