from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import CityClass, Post, Profile
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'Tmy_app/home.html')


class SearchView(TemplateView):
    template_name = "Tmy_app/new_search.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)

        search_value = self.request.GET.get('search', None)
        if search_value:
            context['data'] = CityClass.objects.filter(city_name__icontains=search_value).values('city_name', 'created')
        else:
            context['data'] = CityClass.objects.all().values('city_name', 'created')
        return context


def new_search(request):
    print("request" + str(request))

    queryset = CityClass.objects.all()
    search = request.POST.get('search')
    context = {
        "object_list": queryset,
        "search": search

    }
    return render(request, 'Tmy_app/new_search.html', context)


# .............Cities...........
def moscow_info(request):
    return render(request, 'Tmy_app/moscow_info.html')


def nuremberg_info(request):
    return render(request, 'Tmy_app/nuremberg_info.html')


def lisbon_info(request):
    return render(request, 'Tmy_app/lisbon_info.html')


def madeira_info(request):
    return render(request, 'Tmy_app/madeira_info.html')


# ............NavBar Items....................................
def contacts(request):
    return render(request, 'Tmy_app/contacts.html')


def about_us(request):
    return render(request, 'Tmy_app/about_us.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in.')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'Tmy_app/users/register.html', {'form': form})

@login_required
def feedback_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Tmy_app/users/feedback_page.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'Tmy_app/users/feedback_page.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


@login_required
def profile(request):
    return render(request, 'Tmy_app/users/profile.html')
