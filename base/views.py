from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
# az in ketabkhone baray in estefade mishe ke kesi ke hanoz login nakarde natone hich bakhshi az site ro be joz baksh login bbine,
# dar in ja ma in dastor ro baray safhe home gharar dadim va har kasi vared site she mostaghim toy login page mire
#baray in ke be safhe login befreste bayad dar bakhsh setting ye chenin chizi benevisi: LOGIN_URL = 'login'

from .models import Task
# yeki az bahaliya class base neveshtan ine ke mitoni rahat toy directory app khodet ye dir template va tosh yeki dige be esm
# app mored nazaret dorost koni va badesh har kelasi dorost kobi miyad bar asas nam hamon class barash ye tamplate dar nazar migire
# ke fagat to bayad dorostesh koni va esmesh defaulte vali mitoni mesle paeen avazesh koni.vali khobish ine khodes dir template ro midone.


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


class TaskDetail(LoginRequiredMixin, DetailView):  # namayesh details har object yek user
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'  # hame attribute hay class model ro mikhone
    success_url = reverse_lazy('tasks')
    # in reverse_laze dar asl miyad mige ke bad az ine ke form submit shod bere koja ke ma behesh goftim boro to urli ba name = 'task'


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
    # barau anjam faryand delete niaz dari be ye template ta dar on amal delete ro anjam bedi

