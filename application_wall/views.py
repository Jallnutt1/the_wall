from application_wall.models import Message
from django.shortcuts import render, redirect
from django.apps import apps
from application.models import *
from .models import *

# User = apps.get_model('application', 'User')

def index(request):
    context={
        'user':User.objects.get(id=request.session['userid']),
        'Posted_Messages':Message.objects.order_by('-created_at'),
        'Posted_Comments':Comment.objects.all()
    }
    return render(request,'wall/index.html', context)

def messagePost(request):
    if request.method=="POST":
        currentUser=User.objects.get(id=request.session['userid'])
        thisMessage = Message.objects.create(message=request.POST['message'], user=currentUser)
        return redirect('/wall')

def commentPost(request,id):
    if request.method=="POST":
        currentUser=User.objects.get(id=request.session['userid'])
        currentMessage=Message.objects.get(id=id)
        thisComment = Comment.objects.create(comment=request.POST['comment'], message=currentMessage, user=currentUser)
        return redirect('/wall')

def deleteComment(request,id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('/wall')

def deleteMessage(request,id):
    message = Message.objects.get(id=id)
    message.delete()
    return redirect('/wall')


