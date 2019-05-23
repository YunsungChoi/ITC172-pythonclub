from django.shortcuts import render, get_object_or_404
from .models import Resource
from .models import Meeting

# Create your views here.
def index(request): 
    return render(request, 'club/index.html')

def gettypes(request):
    type_list=Resource.objects.all()
    return render(request, 'club/resources.html' ,{'type_list' : type_list})

def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meetings_list': meetings_list})

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context={
        'meet' : meet,
    }
    return render(request, 'club/meetingdetails.html', context=context)
