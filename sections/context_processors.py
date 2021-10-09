from sections.models import Country, Category


def countries(request):
    context = {"countries": Country.objects.all(),
               "categories": Category.objects.all(),
               }
    return context
