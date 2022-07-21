from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views import generic
from .models import Dome, Category
from .filters import DomeFilter
from .forms import DomeCreation, CategoryCreation
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class ExploreDomesView(generic.ListView):
    template_name = 'domes/explore.html'
    context_object_name = 'domes'
    paginate = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Domes = Dome.objects.filter(privacy=1)
        filter = DomeFilter(self.request.GET, queryset=Domes)
        Domes = filter.qs
        context['domes'] = Domes
        context['filter'] = filter
        return context
        
    def get_queryset(self):
        return Dome.objects.filter(date__lte=timezone.now()).order_by('-date') # [:5]

class DomeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dome
    form_class = DomeCreation
    
    def post(self, request, *args, **kwargs):
        form = DomeCreation(self.request.POST, self.request.FILES)
        if form.is_valid():
            user =self.request.user
            form_pic = form.cleaned_data.get('picture')
            form_banner = form.cleaned_data.get('banner')
            form_title = form.cleaned_data.get('title')
            form_description = form.cleaned_data.get('description')
            form_privacy = form.cleaned_data.get('privacy')
            
            dome,created = Dome.objects.get_or_create(picture=form_pic,banner=form_banner,title=form_title,description=form_description, user = user,privacy=form_privacy )
            dome.save()
            return HttpResponseRedirect(reverse('domes:explore')) #fix url latter
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
            
            
class DomeView(LoginRequiredMixin,UserPassesTestMixin,generic.DetailView):
    model = Dome
    template_name = 'domes/dome_detail.html'
    
    def test_func(self):
        dome_obj = self.get_object()
        dome_members = dome_obj.members.all()
        dome_privacy = dome_obj.privacy
        if (self.request.user in dome_members) | (dome_privacy ==1):
            return True
        return False
    
class CategoryCreateView(LoginRequiredMixin,generic.DetailView, generic.edit.FormMixin):
    model = Dome
    form_class = CategoryCreation
    template_name = 'domes/category_form.html'
    def post(self, request, *args, **kwargs):
        form = CategoryCreation(self.request.POST)
        if form.is_valid():
            dome_obj = get_object_or_404(Dome, pk= self.kwargs.get('pk'))
            title = form.cleaned_data.get('title')
            c = Category(title=title, Dome=dome_obj)
            c.save()
            return HttpResponseRedirect(reverse('domes:dome-detail',args=[dome_obj.pk]))
        