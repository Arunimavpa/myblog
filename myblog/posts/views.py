from django.shortcuts import render
from .models import Create_Post

# Create your views here.
def post_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')   # matches form input name
        create_obj = Create_Post(title=title, content=content)  # <-- use model here
        create_obj.save()
        return render(request, 'post_create.html', {"message": "Post created successfully!"})
    return render(request, 'post_create.html')

def post_list(request):
    posts=Create_Post.objects.all()
    return render(request, 'post_list.html',{'posts':posts}) 

