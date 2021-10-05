from django.http import JsonResponse
from django.views.generic import TemplateView

from sections.models import Question


class BaseView(TemplateView):
    template_name = 'sections/index.html'


class AboutUsView(TemplateView):
    template_name = 'sections/about-us.html'


class HowWorksView(TemplateView):
    template_name = 'sections/how-works.html'


class NewsView(TemplateView):
    template_name = 'sections/news.html'


class DetailNewsView(TemplateView):
    template_name = 'sections/detail-news.html'


class ShopView(TemplateView):
    template_name = 'sections/shop.html'


class FaqView(TemplateView):
    template_name = 'sections/FAQ.html'

    '''AJAX request'''

    def post(self, request):

        data = request.POST
        email = data.get('email')
        phone = data.get('phone')
        name = data.get('name')
        comment = data.get('comment')

        question = Question(email=email, phone=phone,
                            name=name, comment=comment)
        question.save()

        return JsonResponse({'data': True})
