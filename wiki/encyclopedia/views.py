from django.shortcuts import render, redirect
from . import util
from django import forms
from django.urls import reverse

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")

def index(request):
    entries = util.list_entries()
    entry_contents = {}
    for entry in entries:
        entry_contents[entry] = util.get_entry(entry)

    return render(request, "encyclopedia/index.html", {
        "entries": entry_contents
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
    if request.method == "POST":
        new_entry = NewEntryForm(request.POST)
        if new_entry.is_valid():
            title = new_entry.cleaned_data['title']
            content = new_entry.cleaned_data['content']
            existing_entry = util.get_entry(title)
            if existing_entry is not None:
                entry_url = reverse('entry', kwargs={'entry': title})
                return render(request, "encyclopedia/error.html", {
                    "error_message": f"This page already exists. Please update ",
                    "existing_entry_url": entry_url,
                    "existing_entry_title": title
                })
            else:
                util.save_entry(title, content)
                return redirect('entry', entry=title)
    else:
        return render(request, "encyclopedia/new_entry.html",{
        "new_entry": NewEntryForm()
        })
