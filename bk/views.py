from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import Store, Books
from .forms import Store_F, Books_F, Search
import requests
import json


# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm = UserCreationForm()
    return render(request, 'bk/signup.html', {'form': fm})


def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            pas = fm.cleaned_data['password']
            user = authenticate(username=uname, password=pas)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/show1/')
    else:
        fm = AuthenticationForm()
    return render(request, 'bk/login.html', {'forms': fm})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def store(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = Store_F(request.POST)
            if fm.is_valid():
                regis = request.user
                store_name = fm.cleaned_data['store_name']
                loc = fm.cleaned_data['loc']
                s = Store(regis=regis,store_name=store_name,loc=loc)
                s.save()
                # messages.success(request, 'Data added')
                return HttpResponseRedirect('/show1/')
        else:
            fm = Store_F()
        return render(request, 'bk/store.html', {'forms': fm})
    else:
        return HttpResponseRedirect('/login/')


def book(request, idd, id, title, img):
    if request.user.is_authenticated:
        # if request.method == 'POST':
        s = Store.objects.get(id=idd)
        fm = Books.objects.filter(refid=id, store=s)

        if fm:
            print('In else------------------------')
            fm[0].count += 1
            fm[0].save()
        else:
            print('in elelele')
            fm = Books(store=s, refid=id, bookname=title, img=img, count=1)
            fm.save()
        # return HttpResponse('ok')
        return HttpResponseRedirect(f'/show/{idd}')
        # else:
        #     fm = Books_F()
        # return render(request, 'bk/book.html', {'forms': fm})
    else:
        return HttpResponseRedirect('/login/')


def edit_book(request, id):
    if request.user.is_authenticated:
        bk = Books.objects.get(id=id)
        if request.method == 'POST':

            fm = Books_F(instance=bk, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Book added')
        else:
            fm = Books_F(instance=bk)
        return render(request, 'bk/edit.html', {'forms': fm})
    else:
        return HttpResponseRedirect('/login/')


def show_book(request, id):
    if request.user.is_authenticated:
        bk = Books.objects.filter(store=id)
        if not bk.exists():
            messages.success(request, 'Inventory is empty')
        return render(request, 'bk/show.html', {'data': bk, 'idd': id})
        # else:
        #     return HttpResponseRedirect('/store/')
    else:
        return HttpResponseRedirect('/login/')


def show_store(request):
    if request.user.is_authenticated:
        bk = Store.objects.filter(regis=request.user)
        if bk.exists():
            return render(request, 'bk/show1.html', {'data': bk})
        else:
            return HttpResponseRedirect('/store/')
    else:
        return HttpResponseRedirect('/login/')


def del_book(request, id):
    if request.user.is_authenticated:
        Books.objects.get(id=id).delete()
        return HttpResponseRedirect('/show1/')
    else:
        return HttpResponseRedirect('/login/')


def search(request, idd):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = Search(request.POST)
            if fm.is_valid():
                googleapi = 'https://www.googleapis.com/books/v1/volumes?q='
                search = fm.cleaned_data['search']
                googleapi += search
                j = requests.get(googleapi)
                j = j.json()
                print('-----------------------')
                if j['totalItems'] == 0:
                    messages.success(request, 'Book not found')
                else:
                    l1, l2, l3 = [], [], []

                    for i in j['items']:
                        l1.append(i['id'])
                        l2.append(i['volumeInfo']['title'])
                        try:
                            l3.append(i['volumeInfo']['imageLinks']['thumbnail'])
                        except:
                            l3.append('#')

                    d = zip(l1, l2, l3)
                    return render(request, 'bk/insert.html', {'d': d, 'idd': idd})
        else:
            fm = Search()
        return render(request, 'bk/search.html', {'forms': fm})
    else:
        return HttpResponseRedirect('/login/')
