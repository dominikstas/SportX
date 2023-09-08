from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, "login/login.html", context)
    