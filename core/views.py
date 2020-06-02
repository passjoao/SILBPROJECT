from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
import json

from django.views.decorators.csrf import csrf_exempt

from .models import Request, Owner, LandRecord

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

@csrf_exempt
def loaddados(request):
    a = []
    if (request.method == "POST"):
        body_unicode = eval(request.body.decode('utf-8'))
        pesquisa = body_unicode['pesquisa']
        landrecord = LandRecord.objects.filter(reference__contains=pesquisa,location__contains=pesquisa)
        owner = Owner.objects.filter(name__contains=pesquisa,original_name__contains=pesquisa)
        request = Request.objects.filter(requestType__contains=pesquisa)
        f = max([landrecord.count(),owner.count(),request.count()],key=int)
    return HttpResponse(json.dumps(a),content_type='application/json',status=201)

#     dados = []
#     if (request.method == "POST"):
#         body_unicode = eval(request.body.decode('utf-8'))
#         #referencia landrecord - reference
#         re = LandRecord.objects.filter(reference = )
#     #referencia landrecord - reference
#     #localização landrecord - location
#     #Data da Requisição request - dateRequest
#     #Data da concessão confirmation - dateConfirmation
#     #Sesmeiros owner - name, original_name
    #     #Tipo de carta request - requestType