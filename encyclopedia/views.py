import re
import random
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from . import util
from .forms import Create, Edit


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    return render(request, "encyclopedia/wiki.html", {
        "title": title.capitalize(),
        "entry": util.get_entry(title)
    })


def search(request):
    query = util.list_entries()
    query_search = request.GET.get('search').capitalize()

    if util.get_entry(query_search):
        return render(request, "encyclopedia/wiki.html", {
            "title": query_search.capitalize(),
            "entry": util.get_entry(query_search)
        })

    # using list comprehension
    # to get string with substring

    # Search using List Comprehension
    # res = [i for i in query if query_search in i]
    # search using filter method
    # res = list(filter(lambda x: query_search in x, query))
    # search using regular expression
    res = [x for x in query if re.search(query_search, x)]

    # printing result
    print("All strings with given " + query_search + " are : " + str(res))

    return render(request, "encyclopedia/results.html", {
        "title": "Results",
        "entries": res
    })


def create(request):
    form = Create(request.POST)
    if request.method == "POST":
        print("Form Submitted")
        if form.is_valid():
            print("Form Is Valid")
            title = form.cleaned_data.get("title")
            text = form.cleaned_data.get("text")
            if util.get_entry(title):
                print("Existing Entry Found")
                return render(request, "encyclopedia/create.html",
                              {"msg": "Error This Title Already Exists Please Choose another Title"})
            else:
                print("Saving New Entry")
                util.save_entry(title, text)
                return HttpResponseRedirect("wiki/" + title)

    print("Redirecting to create")
    context = {
        "form": form
    }
    return render(request, "encyclopedia/create.html", context)


def edit(request, edit_title):
    form = Edit(request.POST)
    if request.method == "POST":
        print("Form Submitted")
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            print("Saving Entry")
            util.save_entry(title, content)
            print("Redirecting to Edited Page")
            return redirect("wiki/" + title)

    print("Redirecting to Edit Page")
    context = {
        "title": edit_title,
        "entry": util.get_entry(edit_title),
    }
    return render(request, 'encyclopedia/edit.html', context)


def random_page(request):
    entry = random.choice(util.list_entries())
    context = {
        "title": entry,
        "entry": util.get_entry(entry),
    }
    return render(request, "encyclopedia/wiki.html", context)
