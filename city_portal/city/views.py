from django.shortcuts import render


def home(request):
    return render(request, 'city/home.html', {'active': 'home'})


def news(request):
    return render(request, 'city/news.html', {'active': 'news'})


def management(request):
    return render(request, 'city/management.html', {'active': 'management'})


def facts(request):
    return render(request, 'city/facts.html', {'active': 'facts'})


def contacts(request):
    return render(request, 'city/contacts.html', {'active': 'contacts'})


def history(request):
    return render(request, 'city/history.html', {'active': 'history'})


def history_people(request):
    return render(request, 'city/history_people.html', {'active': 'history'})


def history_photos(request):
    return render(request, 'city/history_photos.html', {'active': 'history'})
