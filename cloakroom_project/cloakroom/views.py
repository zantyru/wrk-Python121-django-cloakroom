from django.shortcuts import render, reverse
from django.shortcuts import HttpResponseRedirect
from django.views import generic
from .models import (
    Label
)


class IndexView(generic.ListView):
    template_name = "cloakroom/index.html"
    model = Label
    context_object_name = "label_list"
    extra_context = {
        'title': 'Управление номерками'
    }

    def get_queryset(self):
        return Label.objects.order_by('number')


class UpdateLabelView(generic.View):  #@TODO generic.FormView

    def get(self, request, label_id):

        label = Label.objects.filter(pk=label_id).first()

        if label:
            response = render(
                request,
                "cloakroom/update-label.html",
                {
                    'title': 'Операция над номерком',
                    'label': label,
                    'update_type_url': ''
                }
            )
        else:
            response = HttpResponseRedirect(
                reverse('cloakroom:index')
            )

        return response


class ReturnLabelView(generic.View):

    def post(self, request, label_id):
        pass


class AcquireLabelView(generic.View):

    def post(self, request, label_id):
        pass