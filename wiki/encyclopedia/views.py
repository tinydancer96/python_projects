from django.shortcuts import render, redirect

from . import util


import markdown

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    content = convert_md_to_html(entry)
    if content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "This page entry does not exist"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": entry,
            "content": content
        })

def error(request):
    return render(request, "encyclopedia/error.html")


def new_entry(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })
    return render(request, "encyclopedia/new_entry.html")

def search(request):
    if request.method == "POST":
        search = request.POST.get('q')
        entry = util.get_entry(search)
        if entry == None:
            return render(request, "encyclopedia/error.html", {
                "message": f"'{search}' does not exist"
            })
        else:
            return redirect("entry", entry=search)


def edit(request, entry):
    content = util.get_entry(entry)
    if request.method == "POST":
        return render(request, "encyclopedia/edit.html", {
            "entry": entry,
            "content": content
        })

def save_edit(request, entry):
    content = request.POST.get('content')
    if request.method == "POST":
        util.save_entry(entry, content)
        return redirect("entry", entry=entry)
