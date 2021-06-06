from rest_framework import serializers

from chat_messages.models import UserMessage


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = ('id', 'sender', 'receiver', 'subject', 'body', 'is_new', 'creation_date')
        read_only_fields = ('id', 'sender', 'is_new', 'creation_date')
