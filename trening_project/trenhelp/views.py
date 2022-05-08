from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView, DetailView, CreateView,
                                DeleteView,UpdateView)
from trenhelp.models import Training,Exercise
from trenhelp.forms import CreateUserForm, CreateProfilForm, CreateTrainingForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class TrenhelpHomeView(TemplateView):
    template_name= 'trenhelp/home.html'

class TrenhelpListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Training
    ordering = ['-date_created']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TrenhelpDetailView(DetailView):
    model = Training
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TrenhelpCreateView(CreateView):
    model = Training
    fields = ['name','date_created']

def create_training(request):
    training_form = CreateTrainingForm
    current_user = request.user
    if request.method == 'POST':
        training_form = CreateTrainingForm(request.POST)

        if training_form.is_valid():
            training_form.save(commit=False)
            training_form.instance.user = current_user
            training_form.save()
            return redirect('list_view')
    context = {'form':training_form}
    return render(request,'trenhelp/create_training.html',context)

class TrenhelpDeleteView(DeleteView):
    model = Training
    success_url = reverse_lazy('list_view')

class TrenhelpUpdateView(UpdateView):
    model = Training
    fields = ['name']
    template_name_suffix = '_update_form'

class TrenhelpExerciseUpdateView(UpdateView):
    model = Exercise
    fields = ['name','sets','reps','weight']
    template_name_suffix='_update_form'

class TrenhelpExerciseCreateView(CreateView):
    model = Exercise
    fields = ['training','name','sets','reps','weight']

class TrenhelpExerciseDeleteView(DeleteView):
    model = Exercise
    success_url = reverse_lazy('trenhelp:trenhelp_detail')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('list_view')
        else:
            messages.info(request,'Username or password is incorrect')
    context={}
    return render(request,'trenhelp/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    user_form = CreateUserForm
    profile_form = CreateProfilForm
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        profile_form = CreateProfilForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')

    context={'form':user_form,'form2':profile_form}
    return render(request,"trenhelp/register.html",context)