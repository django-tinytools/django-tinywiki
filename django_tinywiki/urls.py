from django.urls import path,include
from . import views
from . import settings

app_name="tinywiki"

urlpatterns = [
    path("",views.WikiIndexView.as_view(),name="index"),
    path("page/<slug:page>/",views.WikiPageView.as_view(),name="page"),
    path("edit/<slug:page>/",views.WikiEditView.as_view(),name="page-edit"),
    path("create/",views.WikiCreateView.as_view(),name="page-new"),
    path("create/<slug:page>/",views.WikiCreateView.as_view(),name="page-create"),
    #path("image-upload/<slug:page>",views.WikiImageUpload.as_view(),name="image-upload"),
    path("manage/",views.manage.ManageView.as_view(),name="manage"),
    path("manage/init",views.manage.InitializeView.as_view(),name="manage-init"),
    path("manage/page/",views.manage.PageListView.as_view(),name="manage-pagelist"),
    path("manage/page/<slug:page>",views.manage.PageView.as_view(),name="manage-page"),
    path("manage/user/",views.manage.UserListView.as_view(),name="manage-userlist"),
    path("manage/user/<uid>/",views.manage.UserView.as_view(),name="manage-user"),
    #path("manage/image/",views.manage.ImageList.as_view(),name="manage-imagelist"),
    #path("manage/image/orphaned/",views.manage.OrphanedImageList.as_view(),name="manage-image-orphaned")
    #paht("manage/image/<int:id>/",views.manage.Image.as_view(),name="manage-image"),
]

if settings.TINYWIKI_IS_MAIN_APP:
    urlpatterns += [
        path("login/",views.auth.LoginView.as_view(),name="auth-login"),
        path("logout/",views.auth.LogoutView.as_view(),name="auth-logout"),
        path("signup/",views.auth.SignupView.as_view(),name="auth-signup"),
        path("profile/",views.auth.ProfileView.as_view(),name="auth-profile"),
    ]
