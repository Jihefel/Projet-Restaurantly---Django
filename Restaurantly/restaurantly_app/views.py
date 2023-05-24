from django.shortcuts import render
from .models import Member

# Create your views here.

def index(request):
    return render(request, 'restaurantly_app/home.html')

def about(request):
    return render(request, 'restaurantly_app/about.html')

def menu(request):
    return render(request, 'restaurantly_app/menu.html')

def specials(request):
    return render(request, 'restaurantly_app/specials.html')

def events(request):
    return render(request, 'restaurantly_app/events.html')

def chefs(request, name=None):
    chefs = [
        {
            "id": 1,
            "img": "restaurantly_app/img/chefs/chefs-1.jpg",
            "name": "Walter White",
            "status": "Master Chef",
        },
        {
            "id": 2,
            "img": "restaurantly_app/img/chefs/chefs-2.jpg",
            "name": "Sarah Jhonson",
            "status": "Patissier",
        },
        {
            "id": 3,
            "img": "restaurantly_app/img/chefs/chefs-3.jpg",
            "name": "William Anderson",
            "status": "Cook",
        }
    ]

    if name:
        chefs = [chef for chef in chefs if chef['name'] == name]

    return render(request, 'restaurantly_app/chefs.html', {'chefs': chefs})

def gallery(request):
    return render(request, 'restaurantly_app/gallery.html')

def contact(request):
    return render(request, 'restaurantly_app/contact.html')

def book_table(request):
    return render(request, 'restaurantly_app/book_table.html')

def preloader(request):
    return render(request, 'restaurantly_app/preloader.html')

def back_to_top(request):
    return render(request, 'restaurantly_app/back_to_top.html')

def membres(request):
    membres = Member.objects.all()
    nb_membres = membres.count()
    hommes = membres.filter(gender='male')
    femmes = membres.filter(gender='female')
    hommes_condition = hommes.filter(age__range=(18, 24))
    femmes_condition = femmes.filter(age__range=(18, 24))
    personnes_hors_conditions = membres.exclude(age__range=(18, 24))

    context = {
        'membres': membres,
        'nb_membres': nb_membres,
        'hommes': hommes,
        'femmes': femmes,
        'hommes_condition': hommes_condition,
        'femmes_condition': femmes_condition,
        'personnes_hors_conditions': personnes_hors_conditions
    }

    return render(request, 'restaurantly_app/membres.html', context)