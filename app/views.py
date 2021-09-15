from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pymongo.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm,CreateUserForm,DocumentForm
from .decorators import allowed_users, unauthenticated_user
from .resources import resourcessci1
from .resources import reuser
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from tablib import Dataset
from .models import  sci1,Document
from django.conf import settings
from django.core.files.storage import FileSystemStorage



# @login_required(login_url='login')

def dashboard(request):
    # user = User.objects.count()
    # event_ctg = EventCategory.objects.count()
    # event = Event.objects.count()
    # complete_event = Event.objects.filter(status='completed').count()
    # events = Event.objects.all()
    # context = {
    #     'user': user,
    #     'event_ctg': event_ctg,
    #     'event': event,
    #     'complete_event': complete_event,
    #     'events': events
    # }
    return render(request, 'dashboard.html')


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {
        'form': forms
    }
    return render(request, 'login.html', context)


@unauthenticated_user
def registerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'basic_sign_page.html', context)

def upload_csv_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "file saved")
            return render(request,'all_adminhtmlpages/upload_csv.html')
    else:
        form = DocumentForm()
    return render(request, 'all_adminhtmlpages/upload_csv.html', {
        'form': form
    })


    # if request.method == 'POST':
    #     resourcesci1 = resourcessci1()
    #     dataset = Dataset()
    #     new_entity = request.FILES['myfile']
    #
        # imported_data = dataset.load(new_entity.read(), format='xlsx')
        # for data in imported_data:
        #     value = sci1(
        #         data[0],
        #         data[1],
        #         data[2],
        #         data[3]
        #
        #     )
        #     value.save()
    #
    # return render(request,'all_adminhtmlpages/upload_csv.html')
def show_all_files_list(request):
    ef = Document.objects.all()
    if ef:
        return render(request,'all_adminhtmlpages/show_csv_file_list.html',{'form':ef})

def admin_add_persons(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('addpersons')
    context = {'form': form}
    return render(request,'all_adminhtmlpages/add_person.html',context)


def show_view_contact_list(request):
    return render(request,'all_adminhtmlpages/view_contact_list.html')