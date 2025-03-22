from django.contrib.auth import get_user_model, authenticate
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Book

Admin = get_user_model()

# Admin Signup
@method_decorator(csrf_exempt, name="dispatch")
class AdminSignup(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        if Admin.objects.filter(email=email).exists():
            return JsonResponse({"error": "Admin already exists"}, status=400)

        admin = Admin.objects.create_user(username=email, email=email, password=password)
        return JsonResponse({"message": "Admin registered successfully"}, status=201)

# Admin Login
@method_decorator(csrf_exempt, name="dispatch")
class AdminLogin(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        admin = authenticate(username=email, password=password)
        if admin:
            return JsonResponse({"message": "Login successful", "token": "dummy_token"}, status=200)
        return JsonResponse({"error": "Invalid credentials"}, status=401)

# Books CRUD
@method_decorator(csrf_exempt, name="dispatch")
class BookListCreate(View):
    def get(self, request):
        books = list(Book.objects.values())  
        return JsonResponse(books, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        book = Book.objects.create(**data)
        return JsonResponse({"message": "Book added successfully", "id": book.id}, status=201)

@method_decorator(csrf_exempt, name="dispatch")
class BookRetrieveUpdateDelete(View):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            return JsonResponse({"title": book.title, "author": book.author, "isbn": book.isbn, "published_date": str(book.published_date)})
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)

    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            data = json.loads(request.body)
            for key, value in data.items():
                setattr(book, key, value)
            book.save()
            return JsonResponse({"message": "Book updated successfully"})
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return JsonResponse({"message": "Book deleted successfully"})
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)
