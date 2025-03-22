from django.urls import path
from .views import AdminSignup, AdminLogin, BookListCreate, BookRetrieveUpdateDelete

urlpatterns = [
    path("admin/signup/", AdminSignup.as_view(), name="admin_signup"),
    path("admin/login/", AdminLogin.as_view(), name="admin_login"),
    path("books/", BookListCreate.as_view(), name="book_list_create"),
    path("books/<int:pk>/", BookRetrieveUpdateDelete.as_view(), name="book_detail"),
]
