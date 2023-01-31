# app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

# from datetime import datetime, timedelta
from .models import *
from .forms import *

# Convert HTML to markdown
import markdownify


@login_required
def create(request):
    context = {}
    if request.method == "GET":
        form = RecipeForm()
        context["form"] = RecipeForm()
        return render(request, "app/create.html", context)
    elif request.method == "POST" and request.FILES != None:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new = Recipe()
            user = request.user
            new.author = user
            new.name = form["name"].value()
            new.description = form["description"].value()
            new.prep = form["prep"].value()
            new.cook = form["cook"].value()
            new.servings = form["servings"].value()
            new.ingredients = form["ingredients"].value()
            new.directions = form["directions"].value()
            new.notes = form["notes"].value()
            theimg = request.FILES["image"]
            fs = FileSystemStorage()
            filename = fs.save(theimg.name, theimg)
            file_url = fs.url(filename)
            new.image = filename
            new.save()
            return redirect("home")
        else:
            form = RecipeForm()
            context["form"] = RecipeForm()
            return render(request, "app/create.html", context)
    return render(request, "app/create.html", context)


def home(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes,
    }
    return render(request, "app/index.html", context)


def detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    # recipe.ingredients = markdownify(recipe.ingredients)
    # recipe.directions = markdownify(recipe.directions)

    context = {
        "recipe": recipe,
    }
    return render(request, "app/detail.html", context)


@login_required
def update(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {"recipe": recipe}
    if request.method == "GET":
        form = RecipeForm(instance=recipe)
        context["form"] = form
        return render(request, "app/update.html", context)
    elif request.method == "POST" and request.FILES != None:
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("detail", recipe.id)
        else:
            form = RecipeForm(instance=recipe)
            context["form"] = form
            return render(request, "app/update.html", context)
    return render(request, "app/update.html", context)


@login_required
def delete(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if not request.user == recipe.author:
        return redirect("detail", recipe.id)
    else:
        name = recipe.name
        recipe.delete()
        context = {"name": name}
        return render(request, "app/delete.html", context)
