from django.http import HttpResponse


def hello(request, name):
    return HttpResponse(f"<h1>Hello, {name.capitalize()}!</h1>")
