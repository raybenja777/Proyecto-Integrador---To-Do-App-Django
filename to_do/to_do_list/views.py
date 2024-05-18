from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, TemplateView, View
from django.urls import reverse_lazy
from .models import Task
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

class LoginView(FormView):  # Vista de inicio de sesión
    template_name = 'registration/login.html'  # Plantilla de la página de inicio de sesión
    form_class = AuthenticationForm  # Clase de formulario de inicio de sesión
    success_url = reverse_lazy('task_list')  # Redirige a la página de lista de tareas después del inicio de sesión

    def form_valid(self, form):  # Valida el formulario de inicio de sesión
        login(self.request, form.get_user())  # Autentica al usuario
        return super().form_valid(form)
class RegistroView(CreateView):  # Vista de registro de usuario
    form_class = UserCreationForm  # Clase de formulario de registro de usuario
    template_name = 'registro.html'  # Plantilla de la página de registro de usuario

    def form_valid(self, form):  # Valida el formulario de registro de usuario
        form.save()
        return redirect('login')
    
class LogoutView(View):  # Vista de cierre de sesión
    def post(self, request, *args, **kwargs): 
        logout(request) # Cierra la sesión
        return redirect(reverse_lazy('login'))  # Redirige a la página de inicio de sesión después de cerrar sesión

class TaskListView(LoginRequiredMixin, ListView):  # Vista de lista de tareas
    model = Task # Modelo de la lista de tareas
    template_name = 'task_list.html' # Plantilla de la página de lista de tareas
    context_object_name = 'tasks' # Nombre del objeto de la lista de tareas
    
    def get_queryset(self): # Obtiene los datos de la lista de tareas
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView): # Vista de creación de tareas
    model = Task # Modelo de la lista de tareas
    fields = ['title', 'description', 'status'] # Campos de la lista de tareas
    success_url = reverse_lazy('task_list') # Redirige a la página de lista de tareas
    template_name = 'task_form.html' # Plantilla de la página de formulario de tareas
    
    def form_valid(self, form): # Valida el formulario de la lista de tareas
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView): # Vista de actualización de tareas
    model = Task # modelos de la lista de tareas
    fields = ['title', 'description', 'status'] # Campos de la lista de tareas
    template_name = 'task_form.html' # Plantilla de la página de formulario de tareas
    success_url = reverse_lazy('task_list') # Redirige a la página de lista de tareas
    


class TaskDeleteView(LoginRequiredMixin, DeleteView): # Vista de eliminación de tareas
    model = Task # modelos de la lista de tareas
    success_url = reverse_lazy('task_list') # Redirige a la página de lista de tareas
    template_name = 'task_confirm_delete.html' # Plantilla de la página de confirmación de eliminación de tareas




