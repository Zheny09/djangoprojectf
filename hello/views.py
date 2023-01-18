from django.shortcuts import render

from .models import Test


# Create your views here.
def index(request):
    num_test = Test.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_test': num_test}
    )
