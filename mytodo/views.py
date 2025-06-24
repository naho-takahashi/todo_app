from django.shortcuts import redirect, render
from django.views import View
from mytodo.forms import TaskForm
from .models import Task
from django.urls import reverse_lazy

class IndexView(View):
    def get(self, request):
        
        todo_list = Task.objects.all()
        context = {"todo_list": todo_list}
        
        return render(request, "mytodo/index.html", context)
    
index = IndexView.as_view()

class AddView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, "mytodo/add.html", {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        is_valid = form.is_valid()
        
        if is_valid:
            form.save()
            return redirect('/')
        return render(request, 'mytodo/add.html', {'form': form})
    
class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        
        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()
        
        return redirect('/')
    
add = AddView.as_view()

class UpdateView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = Task.objects.get(pk=pk)
        form = TaskForm(instance=task)
        return render(request, "mytodo/update.html", {'form': form, 'task': task})
    
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = Task.objects.get(pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'mytodo/update.html', {'form': form, 'task': task})
    
update = UpdateView.as_view()

class DeleteView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = Task.objects.get(pk=pk)
        return render(request, 'mytodo/delete.html', {'task': task})
    
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = Task.objects.get(pk=pk)
        task.delete()
        return redirect('/')