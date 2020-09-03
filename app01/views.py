from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django import forms
from django.forms import widgets


# Create your views here.
def book(request):
    return HttpResponse('Home page of book')


def home(request):
    return render(request, "ret2.html")


class RegForm(forms.Form):
    user = forms.CharField(max_length=16)
    pwd = forms.CharField(
        min_length=6,
        max_length=12,
        label="密码",
        widget=widgets.PasswordInput(),

    )
    email = forms.EmailField()
    gender = forms.ChoiceField()
    hobby = forms.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "排球")),
        label="爱好",
        initial=[1, 3],

        widget=forms.widgets.CheckboxSelectMultiple.
    )


def reg2(request):
    form_obj = RegForm()
    if request.method == "POST":
        form_obj = RegForm(request.POST)
    if form_obj.is_valid():
        models.UserInfo.objects.create(form_obj.cleaned_data)

    return render(request, "ret2.html", {"form_obj": form_obj})
++++