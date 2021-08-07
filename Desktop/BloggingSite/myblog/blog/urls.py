from django.urls import path
from .views import HomeView, ArticleDetailVieW, AddPostView, UpdatePostView, DeletePostView, AddCategoryView,CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    #path('',views.home, name='home')
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailVieW.as_view(),name='article_detail'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('article/edit/<int:pk>/remove',DeletePostView.as_view(),name='delete_post'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('category_list/',CategoryListView,name='category_list'),
    path('like/<int:pk>',LikeView,name='like_post'),\
    path('artcile/<int:pk>/comment/',AddCommentView.as_view(), name='add_comment')

]

