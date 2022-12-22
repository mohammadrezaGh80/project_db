from django.contrib import admin

from .models import File, Message


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_file',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'sender', 'receiver', 'datetime_sent',)


# @admin.register(FileMessage)
# class FileMessageAdmin(admin.ModelAdmin):
#     list_display = ('file', 'message', )
