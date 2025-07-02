from django.shortcuts import render
from markdown2 import Markdown
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"\"Entry '{title}' does not exist.\"",
            'title': title
        })
    return render(request, "encyclopedia/entry.html", {
        "content": content,
        "entry": Markdown().convert(content), 
        "title": title
    })


def search(request):
    if request.method == "GET":
        entry_search = request.GET['q']
        all_entries = util.list_entries()
        recommendation = []
        for entry in all_entries:
            if entry_search.lower() in entry.lower():
                recommendation.append(entry)

        if len(recommendation) == 1 and recommendation[0].lower() == entry_search.lower():
            content = util.get_entry(recommendation[0])
            return render(request, "encyclopedia/entry.html", {
                "content": content,
                "entry": Markdown().convert(content), 
                "title": recommendation[0]
            })
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": recommendation, 
                'title': recommendation[0] if len(recommendation) > 0 else entry_search
            }) 


def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        if not title or not content:
            return render(request, "encyclopedia/error.html", {
                "message": "\"Title and content cannot be empty.\""
            })
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {
                "message": f"\"An entry with the title '{title}' already exists.\""
            })
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html", {
            "content": content,
            "entry": Markdown().convert(content), 
            "title": title
        })
    
def edit(request):
    if request.method == 'GET':
        title= request.GET['title']
        content = request.GET['content']
        return render(request, "encyclopedia/edit_page.html", {
            'content': content,
            'title': title
        })
    if request.method == 'POST':
        title= request.POST['title']
        content = request.POST['updated_content']
        util.save_entry(title, content)
        return render(request, 'encyclopedia/entry.html', {
            "content": content,
            "entry": Markdown().convert(content),
            "title": title
        } )
    

def random_page(request):
    all_entries = util.list_entries()
    rand_num = random.randint(0, len(all_entries)-1)
    content = util.get_entry(all_entries[rand_num])
    return render(request, 'encyclopedia/entry.html', {
        "content": content,
        "entry": Markdown().convert(content),
        "title": all_entries[rand_num]
    })