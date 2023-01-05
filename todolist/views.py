# todolist/views.py

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseBadRequest
from todolist.models import TaskList
from django.shortcuts import get_object_or_404
from django.urls import reverse

from todolist.forms import TaskForm

def index(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Form is not valid")

    form = TaskForm()
    tasks = TaskList.objects.all().order_by("-created")

    context = {"tasks": tasks, "form": form, "Status": TaskList.StatusChoice}

    return render(request, "index.html", context)

def update_task_status(
    request: HttpRequest, task_id: int, new_status: str
) -> HttpResponse:
 
    if not new_status in TaskList.StatusChoice.values:
        return HttpResponseBadRequest("Invalid status")
 
    task = get_object_or_404(TaskList, id=task_id)
 
    task.status = new_status
    task.save()
 
    success_url = reverse("index")
 
    return HttpResponseRedirect(success_url)

def delete_task(request: HttpRequest, task_id: int) -> HttpResponse:
 
    task = get_object_or_404(TaskList, id=task_id)
    task.delete()
 
    success_url = reverse("index")
 
    return HttpResponseRedirect(success_url)


# Create your views here.
