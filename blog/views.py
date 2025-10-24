from django.shortcuts import render, redirect
from .models import Autor, Categoria, Post
from .forms import AutorForm, CategoriaForm, PostForm, BuscarForm

def home(request):
    posts = Post.objects.order_by('-fecha')[:5]
    return render(request, "blog/home.html", {"posts": posts})

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AutorForm()
    return render(request, "blog/autor_form.html", {"form": form})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CategoriaForm()
    return render(request, "blog/categoria_form.html", {"form": form})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})

def buscar_post(request):
    resultados = []
    termino = ""
    if request.method == "GET":
        form = BuscarForm(request.GET)
        if form.is_valid():
            termino = form.cleaned_data.get("titulo", "")
            if termino:
                resultados = Post.objects.filter(titulo__icontains=termino)
    else:
        form = BuscarForm()
    return render(request, "blog/buscar.html", {"form": form, "resultados": resultados, "termino": termino})
