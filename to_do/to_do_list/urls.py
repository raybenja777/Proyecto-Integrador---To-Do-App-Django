from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, LoginView, LogoutView, RegistroView


urlpatterns = [
    path('', LoginView.as_view(), name='login'), # URL para la página de inicio directamente desde la ruta inicial
    path('login/', LoginView.as_view(), name='login'), # URL para la página de inicio
    path('logout/', LogoutView.as_view(), name='logout'), # URL para cerrar sesión
    path('task/list/', TaskListView.as_view(), name='task_list'), # URL para la lista de tareas
    path('task/create/', TaskCreateView.as_view(), name='task_create'), # URL para la creación de tareas
    path('task/update/', TaskUpdateView.as_view(), name='task_update'), # URL para la actualización de tareas
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'), # URL para la actualización de tareas
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'), # URL para la eliminación de tareas
    path('register/', RegistroView.as_view(), name='register'),
    path('accounts/profile/', TaskListView.as_view(), name='profile'), # URL para el perfil de usuario
    
    
    # Otras URLs...
]