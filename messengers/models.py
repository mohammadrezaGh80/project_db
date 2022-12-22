from django.db import models
from django.contrib.auth import get_user_model


class File(models.Model):
    name = models.CharField(max_length=255)
    content_file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name


class Message(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    datetime_sent = models.DateTimeField(auto_now_add=True)
    del_tag = models.BooleanField(default=False)
    receiver = models.ForeignKey(get_user_model(), related_name='senders', on_delete=models.CASCADE)
    sender = models.ForeignKey(get_user_model(), related_name='receivers', on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='message', null=True)

    def __str__(self):
        return self.title


# class FileMessage(models.Model):
#     file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='messages')
#     message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='files')
