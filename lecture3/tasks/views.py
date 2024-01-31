from django.shortcuts import render
tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
        # "tasks" - this is what the HTML is accessing. the information of this key is determined by it's value pair (the variable)
        # : tasks - this is the variable and contains the information
    })
