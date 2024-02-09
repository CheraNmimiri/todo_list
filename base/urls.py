from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *
# miyay class hay toy view  ro import mikoni inja

urlpatterns = [
    path('register', RegisterPage.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    # miyaym kelasi ke ghare list karay har user ro behesh neshon mide ro url behesh midim.
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    # dar asl ma ye user darim ke be koli data dige vasl shode, ba
    # ba vared kardan har pk ya hamoin forignkey moyad object hay tolid shode har user ro neshon mide.
    path('create/task/', TaskCreate.as_view(), name='task-create'),
    # name ke midim be url hamon baray estefade dar jinja va hyperlink hast***
    path("task/update/<int:pk>/", TaskUpdate.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(),  name='task-delete'),
]
