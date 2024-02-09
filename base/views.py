from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm #baray sakht register
from django.contrib.auth import login #baray sakht register

# az in ketabkhone baray in estefade mishe ke kesi ke hanoz login nakarde natone hich bakhshi az site ro be joz baksh login bbine,
# dar in ja ma in dastor ro baray safhe home gharar dadim va har kasi vared site she mostaghim toy login page mire
#baray in ke be safhe login befreste bayad dar bakhsh setting ye chenin chizi benevisi: LOGIN_URL = 'login'

from .models import Task
# yeki az bahaliya class base neveshtan ine ke mitoni rahat toy directory app khodet ye dir template va tosh yeki dige be esm
# app mored nazaret dorost koni va badesh har kelasi dorost kobi miyad bar asas nam hamon class barash ye tamplate dar nazar migire
# ke fagat to bayad dorostesh koni va esmesh defaulte vali mitoni mesle paeen avazesh koni.vali khobish ine khodes dir template ro midone.

# baray sakht register page
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm  # baray seda zadan module mored niaz baray form register
    redirect_authenticated_user = True  # ejaze redirect mide ba in dastor
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()  # miyad etelaat ro toy datebase zakhire mikone
        if user is not None:  # age dorost bod brizesh be onvan user hal hazer
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
 

class UserLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    # baray in ke dar sorat login kardan va taeed shodan betone redirect kone

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(ListView):  # kolan in class baray namayesh koli data hay har user hast

    model = Task
    # ba in taeen variable dar asl miyad model ro be class vasl mikone
    context_object_name = 'tasks'
    # miyad list az object hat dorost mikone va mitoni barary jinja va for estefade koni

# in function baray ine ke har user data marbot be khodesh ro fagat bbine.
    def get_context_data(self, **kwargs):  # aval tarif mishe va in ke gharare data haye ro be sorat dict bgire
        context = super().get_context_data(**kwargs)  # kolan ye tabe pishfarze ke karesh ine be class data ezafe kone taht onvan context
        context['tasks'] = context['tasks'].filter(user=self.request.user.id)
        # in ja miyad context ro limit mojone be ueerha yani fagat data hau har user ro bar asas name dar database boro begir va namayesh bede.
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TaskDetail(LoginRequiredMixin, DetailView):  # namayesh details har object yek user
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']  # hame attribute hay class model ro mikhone
    success_url = reverse_lazy('tasks')
    # in reverse_laze dar asl miyad mige ke bad az ine ke form submit shod bere koja ke ma behesh goftim boro to urli ba name = 'task'

    def form_valid(self, form):  # dar asl in def miyad va har dade vorodi ro be ye karbar ekhtesas mide age form valid bashe
        form.instance.user = self.request.user  # mige user form ro barabar user login shode gharar bede
        return super(TaskCreate, self).form_valid(form)
    # ta zamani ke ino tarif nakoni hatman bayad user ro ham aval har form vared koni va age mikhay intor nabashe bayad begi ke har form marbot be kodom usere 
    # va in kar ba in function anjam mishe. age nabashe rasamn ta user to taeen nakoni invalid mahsob mishe.

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    # baray task update niazy be tarif ye tempalte dige nist


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = '__all__'
    context_update_name = 'task'
    success_url = reverse_lazy("tasks")
    template_name = 'base/confirm_delete.html'
    # barau anjam faryand delete niaz dari be ye template ta dar on amal delete ro anjam bede
