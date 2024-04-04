from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


@login_required(login_url="login_url")
def employee_view(request):
    template_name = "curd_app/info.html"
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show.html"
    obj = Employee.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def update_view(request, pk):
    obj = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=obj)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = 'curd_app/info.html'
    context = {'form': form}
    return render(request, template_name, context)


def delete_view(request,  pk):
    obj = Employee.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, 'curd_app/confirm.html')
