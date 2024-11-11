from django.shortcuts import render
from .models import Worker

# generate a list of people
def person_list(request):
    workers = Worker.objects.all()
    return render(request, 'workers_list.html', {'workers': workers})
