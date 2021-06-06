from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from chat_messages.models import UserMessage, User

admin.site.register(UserMessage, admin.ModelAdmin)
admin.site.register(User, UserAdmin)
