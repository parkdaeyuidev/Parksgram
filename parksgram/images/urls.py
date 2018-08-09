from django.conf.urls import url
from django.urls import path
from . import views

app_name= "images"
urlpatterns = [
    path("",view=views.Feed.as_view(),name="feed"),
    path("<str:image_id>/like/",view=views.LikeImage.as_view(),name="like_image"),
    path("<str:image_id>/like/",view=views.UnLikeImage.as_view(),name="like_image"),
    path("<str:image_id>/comment/",view=views.CommentOnImage.as_view(),name="comment_image"),
    path("comments/<str:comment_id>/",view=views.Comment.as_view(),name="comment"),
    path("search/",view=views.Search.as_view(),name="search")
]