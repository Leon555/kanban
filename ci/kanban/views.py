from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from kanban.models import PClint,CodeDex

# Create your views here.
def index(request):
    pclint_list = PClint.objects.all()
    codedex_list = CodeDex.objects.all()
    return render(request, "index.html", {"pclints":pclint_list,"codedexs":codedex_list})
