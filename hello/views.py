from django.conf import settings
from django.shortcuts import render

from .models import Test


# Create your views here.
def index(request):
    num_test = Test.objects.all().count()

    pr = settings.DEBUG

    return render(
        request,
        'index.html',
        context={'num_test': num_test, 'pr': pr}
    )
