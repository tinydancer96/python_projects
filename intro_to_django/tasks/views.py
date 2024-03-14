from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task:")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
        # "tasks" - this is what the HTML is accessing. the information of this key is determined by it's value pair (the variable)
        # : tasks - this is the variable and contains the information
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
