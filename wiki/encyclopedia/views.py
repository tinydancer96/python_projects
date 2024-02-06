from django.shortcuts import render
from . import util
from django import forms


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    entry_content = util.get_entry(entry)
    return render(request, "encyclopedia/entry.html", {
        "entry_title": entry,
        "entry_content": entry_content
    })

def query(request):
    query_param = request.GET.get('query', '')
    query_content = util.get_entry(query_param)
    return render(request, "encyclopedia/query.html", {
        "query_title": query_param,
        "query_content": query_content
    })

def new_entry(request):
    return render(request, "encyclopedia/new_form.html")
