from sections.models import Country


def countries(request):
    context = {"countries": Country.objects.all(),
               }
    return context
