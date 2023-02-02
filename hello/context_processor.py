from django.conf import settings


def admin(request):
    pr = str(settings.DEBUG)
    return {
        'adm': "DEBUG: " + pr
    }
