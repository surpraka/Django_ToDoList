from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from main.models import m1
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    todo_items = m1.objects.all().order_by("-added_date")
    db_stuff = {
        "todo_items": todo_items
    }
    return render(request, 'main/index.html',db_stuff)

@csrf_exempt
def add_todo(request):
    curr_date = timezone.now()
    content = request.POST["content"]
    m1.objects.create(added_date=curr_date,text=content)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, m1_id):
    m1.objects.get(id=m1_id).delete()
    return HttpResponseRedirect("/")