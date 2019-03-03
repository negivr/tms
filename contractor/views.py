from django.shortcuts import render
from .models import Person, Contractor


def contractor(request):

    contractors = Contractor.objects.all()

    context = {
        'contractors': contractors
    }
    return render(request, 'contractor/contractors.html', context)


def people(request):
    persons = Person.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'contractor/people.html', context)


