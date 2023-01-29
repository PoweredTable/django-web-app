from django.shortcuts import render

# Create your views here.

posts = [
    {
        "author": "Person 1",
        "title": "Title 1",
        "content": "First content",
        "date_posted": "28 August 2018"
    },
    {
        "author": "Person 2",
        "title": "Title 2",
        "content": "Second content",
        "date_posted": "29 August 2018"
    }
]


def home(request):
    context = {"posts": posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {"title": "Super Title"})
