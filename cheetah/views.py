from django.shortcuts import render
from util import convertor


# Create your views here.
def index(request):
    if request.method == 'GET':
           convertor.main()
    return render(request,'cheetah/index.html',)

       