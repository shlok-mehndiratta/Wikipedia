from django.shortcuts import render
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
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

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        all_entries = util.list_entries()
        recommendation = []
        for entry in all_entries:
            if entry_search.lower() in entry.lower():
                recommendation.append(entry)

        if len(recommendation) == 1 and recommendation[0].lower() == entry_search.lower():
            content = util.get_entry(recommendation[0])
            return render(request, "encyclopedia/entry.html", {
                "entry": markdown.Markdown().convert(content), 
                'title': entry_search
            })
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": recommendation, 
                'title': entry_search
            }) 
