from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,webpage,AccessRecord
from first_app import forms
# Create your views here.
def index(req):
    weblist = AccessRecord.objects.order_by('date')
    my_dict = {'access_record':weblist}
    return render(req,'index.html',context=my_dict)
def help(req):
    vpas = {'help': 'This has been redirect form help page'}
    return render(req,'help.html',context=vpas)
def form_page(req):
    form = forms.formName()
    if req.method=='POST':
        form = forms.formName(req.POST)
        if form.is_valid():
            print("validation success")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])
    return render(req,'form_page.html',{'form':form})