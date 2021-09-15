from django.shortcuts import render
from django.views.generic import View

# Create your views here.

#def home(request):

    # return render(request, 'index.html')

class BaseView(View):
    pass

class HomeView(BaseView):
    def get(self, request):

        return render(request, 'index.html')
