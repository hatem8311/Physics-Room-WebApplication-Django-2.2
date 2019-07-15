from django.urls import path
from .views import (
    create_post_view,
    comment_to_post_view,
    post_details_view,
    postslistview,
    search_view,
    edit_posts,
    delete_posts)
app_name = 'posts'
urlpatterns=[
    path('create/' , create_post_view , name ='creat_post'),
    path('',postslistview),
    path('comment/<int:id>' ,comment_to_post_view  , name = 'comment'),
    path('<int:id>/' , post_details_view,name='details' ),
    path('search/' , search_view),
    path('edit/<int:id>',edit_posts),
    path('delete/<int:id>',delete_posts),

]