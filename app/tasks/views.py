from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    if "tasks" not in request.session: # 세션에 따라 다른 리스트를 보여주고 싶을 때
        request.session["tasks"] = []
    context = {
        "tasks" : request.session["tasks"]
    }
    return render(request, "tasks/index.html", context)

def add (request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"] # 클래스 객체로 받은 form, 웹에서 전송받은 데이터를 저장해서 보여주는데 어떤걸 보여주느냐 = task (클래스 필드)
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:tasks"))
        else:
            return render(request,"tasks/add.html", {"form":form}) # 에러가 있는 form 페이지 그대로 보여주기 (새 폼 말고)

    context = {
        "form" : NewTaskForm()
    }
    return render(request, "tasks/add.html", context)
