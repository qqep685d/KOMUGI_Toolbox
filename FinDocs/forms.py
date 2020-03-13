from django import forms

import re

from .models import *

class DocForm(forms.ModelForm):

    class Meta:
        model = Doc
        fields = (
            'title', 'type', 'content', 'date',
            'contact_to', 'is_public', 'url', 'image',
            'barcode', 'original', 'backup', 'keywords',
        )
        widgets = {
            'title'    : forms.TextInput(attrs={'size':'60'}),
            'content'  : forms.Textarea(attrs={'rows':4,'cols':60}),
            'date'     : forms.DateInput(attrs={"type":"date",'min':'1900-01-01','max':'2199-12-31'}),
            'url'      : forms.URLInput(attrs={'size':'60'}),
            'image'    : forms.URLInput(attrs={'size':'60'}),
            'backup'   : forms.TextInput(attrs={'size':'60'}),
            'keywords' : forms.Textarea(attrs={'rows':4,'cols':60}),
            # 'is_public': forms.RadioSelect(),
        }


class FilterForm(forms.ModelForm):
    keywords = forms.CharField(initial='', label='キーワード', required = False,)
    class Meta:
        model = Doc
        fields = ('type', 'date')

class DocTypeForm(forms.ModelForm):

    class Meta:
        model = DocType
        fields = ('name', 'priority', 'remarks')
        widgets={
            'name'    : forms.TextInput(attrs={'size':'60'}),
            'priority': forms.NumberInput(attrs={'min':'0'}),
            'remarks' : forms.Textarea(attrs={'rows':4,'cols':60}),
        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('contact_to', 'email', 'priority', 'remarks')
        widgets={
            'contact_to': forms.TextInput(attrs={'size':'60'}),
            'email'     : forms.EmailInput(attrs={'size':'60'}),
            'priority': forms.NumberInput(attrs={'min':'0'}),
            'remarks' : forms.Textarea(attrs={'rows':4,'cols':60}),
        }

class OriginalDocPlaceForm(forms.ModelForm):

    class Meta:
        model = OriginalDocPlace
        fields = ('place', 'priority', 'remarks')
        widgets={
            'place'   : forms.TextInput(attrs={'size':'60'}),
            'priority': forms.NumberInput(attrs={'min':'0'}),
            'remarks' : forms.Textarea(attrs={'rows':4,'cols':60}),
        }

class DocUploadForm(forms.Form):
    name = forms.HiddenInput()
