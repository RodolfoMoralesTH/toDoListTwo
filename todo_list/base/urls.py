from django.urls import path
from .views import CustomLoginView, RegistrationPage, TaskCreate, TaskList, TaskUpdate, DeleteView, TaskDetail
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', RegistrationPage.as_view(), name='register'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name="task-delete"),
]