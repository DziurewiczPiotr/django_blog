from django.shortcuts import render

def blog_home(request):
    data = {
        "page_title": "Thats a title",
        "posts": [
            {
                "title": "ABC",
                "id": 1,
                "content": "Some data"
            },
            {
                "title": "DEF",
                "id": 2,
                "content": "Some more data"
            }
        ]
    }
    return render(request, "blog/home.html", context=data, status=200)

def blog_about(request):
    return render(request, "blog/about.html", status=200)
