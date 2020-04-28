from django.shortcuts import render
from django.views import generic
from .models import Request, Owner

def index(request):
    """View function for home page of site."""

    qtd_captancy = Request.objects.all().count()
    qtd_register = Owner.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'totalRegister': qtd_captancy,
        'totalRegisterQtd': qtd_register,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

from .forms import RequestSearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter

class RequestFilter(BaseFilter):
    search_fields = {
        'search_text' : ['comments', 'privileged_observations']
    }

class RequestListViews(SearchListView):
    model = Request
    paginate_by = 30
    template_name = "core/request_list.html"
    form_class = RequestSearchForm
    filter_class = RequestFilter

class RequestDetailView(generic.DetailView):
    model = Request