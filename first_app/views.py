from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,webpage,AccessRecord
# Create your views here.
def index(req):
    weblist = AccessRecord.objects.order_by('date')
    my_dict = {'access_record':weblist}
    return render(req,'index.html',context=my_dict)
def help(req):
    vpas = {'help': 'This has been redirect form help page'}
    return render(req,'help.html',context=vpas)