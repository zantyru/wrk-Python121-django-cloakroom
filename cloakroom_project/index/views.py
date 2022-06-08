from django.views import generic
from django.shortcuts import render


class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "index/index.html"
        )
