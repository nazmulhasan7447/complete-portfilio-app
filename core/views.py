from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import homePageInfo



def loginToDashboard(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            try:
                user = User.objects.get(username=username)
                if user:
                    authenticate_user = authenticate(username=username, password=password)
                    if authenticate_user is not None:
                        login(request, authenticate_user)
                        return redirect('home')
            except:
                messages.warning(request, "Can't be logged in. Please try again!")
                return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'login.html')


def logoutFromDashboard(request):

    logout(request)

    return redirect('login')


@login_required(login_url='/dashboard/login')
def index(request):

    return render(request, 'index.html')


@login_required(login_url='/dashboard/login')
def home(request):

    return render(request, 'home.html')


@login_required(login_url='/dashboard/login')
def home_page(request):

    if request.method == 'POST':
        coverImg = request.FILES['pic']
        email = request.POST['email']
        linkedin = request.POST['linkedin']
        instagram = request.POST['instagram']
        headline = request.POST['headline']
        additionalInfo = request.POST['additionalInfo']

        if coverImg and email and linkedin and instagram:
            saveToDB = homePageInfo(coverImg=coverImg, email=email, linkedIn=linkedin, instagram=instagram, headline=headline, additionalInfo=additionalInfo)
            saveToDB.save()
            messages.success(request, "Successfully saved")
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.warning(request, "Can not saved. Try again please!")
            return redirect(request.META.get('HTTP_REFERER'))

    homePageInfoList = homePageInfo.objects.all()

    context = {
        'homePageInfo': homePageInfoList
    }


    return render(request, 'homePageSetting.html', context)

@login_required(login_url='/dashboard/login')
def editHomePageInfo(request, pk):

    currentObject = homePageInfo.objects.get(pk=pk)

    if request.method == 'POST':
        email = request.POST['email']
        linkedin = request.POST['linkedin']
        instagram = request.POST['instagram']
        headline = request.POST['headline']
        additionalInfo = request.POST['additionalInfo']

        try:
            coverImg = request.FILES['pic']
            if coverImg:
                currentObject.coverImg = coverImg
                currentObject.email = email
                currentObject.linkedIn = linkedin
                currentObject.instagram = instagram
                currentObject.headline = headline
                currentObject.additionalInfo = additionalInfo
                currentObject.save()
                messages.success(request, "Successfully updated")
                return redirect('home_page')
        except:
            currentObject.email = email
            currentObject.linkedIn = linkedin
            currentObject.instagram = instagram
            currentObject.headline = headline
            currentObject.additionalInfo = additionalInfo
            currentObject.save()
            messages.success(request, "Successfully updated")
            return redirect('home_page')

    context = {
        'currentObject': currentObject,
        'pk': pk
    }
    return render(request, 'edit/editHomePageInfo.html', context)


@login_required(login_url='/dashboard/login')
def removeHomePageInfo(request, pk):

    try:
        currentObject = homePageInfo.objects.get(pk=pk)
        fs = FileSystemStorage()

        fs.delete(currentObject.coverImg.name)
        currentObject.delete()
        messages.success(request, "Successfully deleted")
        return redirect('home_page')
    except:
        messages.warning(request, "Can't be deleted. Try again please!")
        return redirect('home_page')

    return redirect('home_page')













