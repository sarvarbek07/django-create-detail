from django.shortcuts import render,redirect
from .models import HomeModel
from django.views.generic import ListView,DetailView,CreateView
from .forms import ReservationsForm


class Home(ListView):
    template_name="home.html"
    model=HomeModel

class Detail(DetailView):
    template_name="detail.html"
    model=HomeModel

def add(request):
    form=ReservationsForm()
    if request.method=="POST":
        form=ReservationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context={'form':form}
    return render(request,'add.html',context)