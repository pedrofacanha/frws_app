from django.shortcuts import render,redirect
from .models import Worker
from .forms import WorkerForm

# generate a list of people
def person_list(request):
    workers = Worker.objects.all()
    return render(request, 'workers_list.html', {'workers': workers})

# display the form
def worker_form(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workers_list')  # redirect after successful form submission
    else:
        form = WorkerForm()
    return render(request, 'workers_form.html', {'form': form})
