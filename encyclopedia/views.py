from django.shortcuts import render
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"Entry '{title}' does not exist.", 
            'title': title
        })
    return render(request, "encyclopedia/entry.html", {
        "entry": markdown.Markdown().convert(content), 
        'title': title
    })