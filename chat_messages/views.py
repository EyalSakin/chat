from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from django_filters import rest_framework as filters

from chat_messages.serializers import MessageSerializer
from chat_messages.models import UserMessage


class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('is_new',)

    def get_queryset(self):
        queryset = UserMessage.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user))
        return queryset

    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(sender=request.user)
        return Response(serializer.data)


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = UserMessage.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user))
        return queryset

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_new = False
        instance.save()
        serializer = MessageSerializer(instance)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
