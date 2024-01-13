from django.urls import path,include
from . import views
from . import settings

app_name="tinywiki"

urlpatterns = [
    path("",views.WikiIndexView.as_view(),name="index"),
    path("page/<slug>/",views.WikiPageView.as_view(),name="page_view"),
    path("edit/<slug>/",views.WikiEditView.as_view(),name="page_edit"),
    path("create/<slug>/",views.WikiCreateView.as_view(),name="page_create"),
    path("login/",views.auth.LoginView.as_view(),name="auth-login"),
    path("logout/",views.auth.LogoutView.as_view(),name="auth-logout"),
    path("register/",views.auth.SignupView.as_view(),name="auth-register"),
    path("profile/",views.auth.ProfileView.as_view(),name="auth-profile")
    #path("manage/",views.ManageView.as_view(),name="manage"),
    #path("manage/page/",views.ManagePageListView.as_view(),name="manage-pagelist"),
    #path("manage/page/<slug>",views.ManagePageView.as_view(),name="manage-page"),
    #path("manage/user/",views.ManageUserListView.as_view(),name="manage-userlist"),
    #path("manage/user/<string>/",views.ManageUserView.as_view(),name="manage-user"),
]
