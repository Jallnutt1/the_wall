from django.db import models

class Message(models.Model):
    message=models.TextField()
    user=models.ForeignKey('application.User', related_name="message", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment=models.TextField()
    message=models.ForeignKey(Message, related_name="comment", on_delete=models.CASCADE)
    user=models.ForeignKey('application.User', related_name="comment", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

