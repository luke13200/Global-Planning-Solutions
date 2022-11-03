from django.shortcuts import render

# Create your views here.

def index_view(request):
    """
    URL: /
    this view is for the static landing page.
    """
    return render(request, 'user/index.html', None);
