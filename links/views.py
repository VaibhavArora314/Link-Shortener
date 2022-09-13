from django.shortcuts import render,redirect
from django.views.generic import RedirectView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Link
from .forms import CreateLinkform

class RedirectLink(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if Link.objects.filter(tag = kwargs.get('tag')).exists():
            link = Link.objects.get(tag = kwargs['tag'])
            link.visits += 1
            link.save()
            return link.original_link
        return redirect(to='links:not-found').url


def NotFound(request):
    return render(request,'links/not_found.html',{})


class CreateLink(CreateView):
    template_name = 'links/create_link.html'
    context_object_name = 'links'
    form_class = CreateLinkform
    
    def form_valid(self, form):
        self.object = form.save()
        if self.request.user.is_authenticated:
            link = Link.objects.get(tag = form.instance.tag)
            link.user = self.request.user
            link.save()
        # Does not redirect if valid
        #return HttpResponseRedirect(self.get_success_url())

        # Render the template
        # get_context_data populates object in the context 
        # or you also get it with the name you want if you define context_object_name in the class
        return self.render_to_response(self.get_context_data(form=form,shortened_url=str(self.request.build_absolute_uri('/shortener/' + form.instance.tag + '/'))))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortened_url'] = kwargs.get('shortened_url')
        return context


class ListLink(LoginRequiredMixin,ListView):
    context_object_name = 'links'
    template_name = 'links/my_links.html'
    paginate_by = 5

    def get_queryset(self):
        return Link.objects.filter(user = self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prefix'] = self.request.build_absolute_uri('/shortener/')
        return context