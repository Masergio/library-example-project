from django.db import models


class Chat(models.Model):
    chat_id = models.PositiveIntegerField(unique=True)
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chat_id} ({self.username})"


class Message(models.Model):
    chat = models.ForeignKey("Chat", on_delete=models.DO_NOTHING)
    message_id = models.PositiveIntegerField()
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.pk} from ({self.chat})"

