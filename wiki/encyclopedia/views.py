from django.shortcuts import render

from . import util

from markdown2 import Markdown

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        markdowner.convert(content)

def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def entry(request, entry):
    title = util.get_entry(entry)
    return render(request, "encyclopedia/entry.html", {
        "entry": title
    })
