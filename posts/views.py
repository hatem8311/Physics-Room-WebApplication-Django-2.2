from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .forms import post_create_form,comments_to_post_form,EditPostForm
from django.shortcuts import get_object_or_404
from .models import Posts
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


def edit_posts(reqeust,id):
    object = get_object_or_404(Posts , pk=id)
    if reqeust.user == object.author:
        form = EditPostForm(instance=object)
        if reqeust.method=="POST":
            form = EditPostForm(reqeust.POST , instance=object)
            if form.is_valid():
                form.save()
                return redirect(reverse('success'))
        context = {'form':form}
        return render(reqeust,'posts/editpost.html',context)
    else:
        return HttpResponse('you can not edit posts that are not yours')



def delete_posts(reqeust,id):
    object = get_object_or_404(Posts , pk=id)
    if reqeust.user == object.author:
        if reqeust.method=="POST":
            object.delete()
            return redirect(reverse('success'))
        return render(reqeust,'posts/deleteposts.html')
    else:
        return HttpResponse('you can not edit posts that are not yours')
    
def postslistview(request):
    posts = Posts.objects.all()
    context={'posts':posts}
    return render(request , 'posts/posts_list.html' , context)




@login_required(redirect_field_name='/users/login')
def post_details_view(request , id):
    post = get_object_or_404(Posts , id=id)
    comments = Posts.objects.get(id=id).comments_set.all()
    context = {'post': post , 'comments':comments}
    return render(request ,'posts/post_details.html',context)





@login_required(redirect_field_name='/users/login')
def create_post_view(request):
    if request.method =='POST':
        form= post_create_form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect(reverse('success'))
    else:
        form = post_create_form()

    context = {'form':form}

    return render(request , 'posts/post_create_form.html' ,context)

@login_required(redirect_field_name='/users/login')
def comment_to_post_view(request,id):
    post = get_object_or_404(Posts,id =id)
    if request.method=='POST':
        form= comments_to_post_form(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.related_post=post
            instance.related_user=request.user
            instance.save()
            return redirect(reverse('success'))
    else:
        form = comments_to_post_form()

    post_id = post.id

    return render(request , 'posts/comments.html',context={'form':form,'post_id':post_id})

def search_view(request):
    if request.method=='GET':
        print(request.GET['searchino'])
        objects = Posts.objects.filter(title__icontains=request.GET['searchino'])
        print(objects)
        context = {'objects':objects }
        return render(request,'posts/search_results.html' , context)




# Create your views here.
