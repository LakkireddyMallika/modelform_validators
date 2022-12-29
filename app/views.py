from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def insert_topic(request):
    form=TopicForm()
    d={'form':form}
    if request.method=='POST':
        formdata=TopicForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            return HttpResponse('insert_topic is done')

        
    return render(request,'insert_topic.html',d)