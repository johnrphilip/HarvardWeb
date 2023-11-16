from django.shortcuts import render, redirect
from django.http import Http404
from . import util
import markdown2

# Your existing index function
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Your existing entry function
def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        raise Http404("Entry not found")
    html_content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })

# Add the search view function here
def search(request):
    query = request.GET.get('q', '')
    entries = util.list_entries()
    if query in entries:
        return redirect('entry', title=query)
    else:
        matching_entries = [entry for entry in entries if query.lower() in entry.lower()]
        return render(request, "encyclopedia/search_results.html", {
            "entries": matching_entries,
            "query": query
        })
