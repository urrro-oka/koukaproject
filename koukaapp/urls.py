from django.urls import path
from . import views

app_name = 'koukaapp'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('post/',views.CreatePhotoView.as_view(),name='post'),
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
    path('diary/<int:category>',views.CategoryView.as_view(),name='diary_cat'),
    path('user-list/<int:user>',views.UserView.as_view(),name='user_list'),
    path('blog-detail/<int:pk>/',views.BlogDetail.as_view(),name='detail'),
    path('about/',views.aboutView.as_view(),name='about'),
    path('mypage/',views.MypageView.as_view(),name='mypage'),
    path('diary/<int:pk>/delete',views.DiaryDeleteView.as_view(),name='diary_delete'),
    path('contact/',views.ContactView.as_view(),name= 'contact'),
]