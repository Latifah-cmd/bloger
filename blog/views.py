from django.shortcuts import render, redirect
from blog.forms import AuthourForm
from blog.models import Authour

def index_view (request):
    return render(request,'index.html')

def blog_list_view(request):
    return render(request,'blog_list.html')

def  add_authour_view(request):
    message =''
    if request.method =="POST":
        author_from = AuthourForm(request.POST)
        if author_from.is_valid():
            author_from.save()

            message = "Author added successfully"
    else:
        author_from = AuthourForm()

    authours = Authour.objects.all()

    context ={
        'form':author_from,
        'msg': message,
        'authours': authours
    }
    return render(request,"add_authour_.html",context)
def edit_authour_view(request,authour_id):
    message=''
    authour =  Authour.objects.get(id=authour_id)

    if request.method == "POST":
        authour_form = AuthourForm(request.POST,instance=authour)

        if authour_form.is_valid():
            authour_form.save()
            message = "changes saved successfully!"

        else:
            message = "form has invalid data"

    else:
        authour_form = AuthourForm(instance=authour)

    context = {
        'form': authour_form,
        'authour': authour,
        'message':message,
        
    }

    return render (request,'edit_authour.html',context)

def delete_authour_view(request, authour_id):
    authour = Authour.objects.get(id=authour_id)

    authour.delete()

    return redirect(add_authour_view)