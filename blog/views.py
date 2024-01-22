from django.shortcuts import render, redirect, get_object_or_404
from .forms import Post
from .forms import SignupForm, LoginForm


# Create your views here.
def index(request):
    post = Post.objects.all()
    context = {"post": post}
    return render(request, "blog/home.html", context)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("blog:index")
    else:
        form = SignupForm()

    return render(request, "blog/signup.html", {
        "form": form
    })

def login(request):
  return render(request, "blog/login.html")