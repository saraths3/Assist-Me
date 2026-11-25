from django.http import HttpResponse

def home(request):
    return HttpResponse(f"Logged in as: {request.user}")
