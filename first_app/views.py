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
def sign_up(req):
        User_info_form = forms.UserProfileInfoForm()
        User_form = forms.UserProfileForm()
        if req.method == 'POST':
                User_form = forms.UserProfileForm(data=req.POST)
                User_info_form = forms.UserProfileInfoForm(data=req.POST)
                if User_form.is_valid() and User_info_form.is_valid():
                        user = User_form.save()
                        user.set_password(user.password)
                        user.save()
                        #saving user form
                        profile = User_info_form.save(commit=False)
                        profile.user = user
                        if 'profile_picture' in req.FILES:
                                profile.profile_pic = req.FILES['profile_picture']
                        else:
                                print("No Profile Pic")
                        profile.save()
                else:
                        print("Form is not Valid")
        return render(req,'index.html',{'form':User_form,'form1':User_info_form})