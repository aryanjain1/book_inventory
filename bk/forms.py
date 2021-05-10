from django import forms
from .models import Store, Books


class Store_F(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["store_name","loc"]

        labels = {'store_name': 'Store ',
                  'loc': 'Location'}


class Books_F(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        labels = {'bookname': 'Title of book',
                  'count': 'No. of book'}

class Search(forms.Form):
    search = forms.CharField(max_length=1000)