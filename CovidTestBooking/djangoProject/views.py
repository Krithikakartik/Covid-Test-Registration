from random import randint

from django import forms
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from Tester import models


def reservation(request):
    if request.method == "POST":
        uid = randint(100000, 999999)
        user = models.user.objects.create(id=str(uid), userTpye=request.POST.get('userType'),
                                          userName=request.POST.get('userName1') + ' ' + request.POST.get('userName2'),
                                          userEmail=request.POST.get('userEmail'),
                                          userDate=request.POST.get('userDate'), userTime=request.POST.get('userTime'),
                                          userResult='yes', userSyp=request.POST.get('userSyp'),
                                          userAge=request.POST.get('userAge'), userPhone=request.POST.get('userPhone'),
                                          userGander=request.POST.get('userGander'),
                                          userVac=request.POST.get('userVac'))
        print(user)
        user.save()
        messages.success(request, "register successfully,your ID is" + str(id))
        return render(request, 'return.html')

    else:
        return render(request, 'dist/index.html')





