from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.db.models import Sum
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework import viewsets
from enum import *

from .serializers import *

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


class RequestViewset(viewsets.ModelViewSet):

    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class AuthorityViewset(viewsets.ModelViewSet):
    queryset = Authority.objects.all()
    serializer_class = AuthoritySerializer


class CaptaincyViewset(viewsets.ModelViewSet):
    queryset = Captaincy.objects.all()
    serializer_class = CaptaincySerializer


class ConfirmationViewset(viewsets.ModelViewSet):
    queryset = Confirmation.objects.all()
    serializer_class = ConfirmationSerializer


class DefermentViewset(viewsets.ModelViewSet):
    queryset = Deferment.objects.all()
    serializer_class = DefermentSerializer


class DemandsViewset(viewsets.ModelViewSet):
    queryset = Demands.objects.all()
    serializer_class = DemandsSerializer


class FilesViewset(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer


class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class JustificationViewset(viewsets.ModelViewSet):
    queryset = Justification.objects.all()
    serializer_class = JustificationSerializer


class LandRecordViewset(viewsets.ModelViewSet):
    queryset = LandRecord.objects.all()
    serializer_class = LandrecordSerializer


class OwnerViewset(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class ReligiousOrderViewset(viewsets.ModelViewSet):
    queryset = ReligiousOrder.objects.all()
    serializer_class = ReligiousOrderSerializer


class TramitationsViewset(viewsets.ModelViewSet):
    queryset = Tramitations.objects.all()
    serializer_class = TramitationsSerializer

class RequestFilter(BaseFilter):
    search_fields = {
        'search_text': ['comments', 'privileged_observations', 'record_id__location']
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
    if request.method == "GET":
        body_unicode = eval(request.body.decode('utf-8'))
        pesquisa = body_unicode['pesquisa']
        landrecord = LandRecord.objects.filter(location__icontains=pesquisa)
        owner = Owner.objects.filter(name__contains=pesquisa, original_name__icontains=pesquisa)
        request = Request.objects.filter(reference__contains=pesquisa, requestType__icontains=pesquisa)
        f = max([landrecord.count(), owner.count(),request.count()],key=int)
    return HttpResponse(json.dumps(a), content_type='application/json',status=201)