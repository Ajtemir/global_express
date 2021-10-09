from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, Http404
from django.views.generic import TemplateView, ListView, DetailView

from sections.filters import ShopFilter, NewsFilter
from sections.models import Question, Shop, News, AboutUsInformation, HowItWorks, FaqBlock


class BaseView(TemplateView):
    template_name = 'sections/index.html'


class AboutUsView(TemplateView):
    template_name = 'sections/about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = AboutUsInformation.objects.first()
        return context


class HowWorksView(TemplateView):
    template_name = 'sections/how-works.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = HowItWorks.objects.first()
        return context


class NewsListView(ListView):
    template_name = 'sections/news.html'
    model = News
    context_object_name = 'news_list'
    filterset_class = NewsFilter
    paginate_by = 3

    def get_queryset(self):
        if self.request.is_ajax():
            self.template_name = 'sections/news-object.html'
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_list = self.filterset_class(self.request.GET,
                                         queryset=self.get_queryset())
        pagination = Paginator(news_list.qs, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            news_list = pagination.page(page)
        except PageNotAnInteger:
            news_list = pagination.page(1)
        except EmptyPage:
            raise Http404("That page contains no results")

        context['news_list'] = news_list.object_list
        context['category_id'] = self.request.GET.get('category')
        context['page_obj'] = news_list

        return context


class DetailNewsView(DetailView):
    template_name = 'sections/detail-news.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other_news = self.model.objects.exclude(id=context['object'].id).order_by('-id')[:3]
        context['other_news'] = other_news
        return context


class ShopListView(ListView):
    template_name = 'sections/shop.html'
    model = Shop
    context_object_name = 'shops'
    filterset_class = ShopFilter
    paginate_by = 3

    def get_queryset(self):
        if self.request.is_ajax():
            self.template_name = 'sections/shop-detail.html'
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop_list = self.filterset_class(self.request.GET, queryset=self.get_queryset())
        pagination = Paginator(shop_list.qs, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            shop_list = pagination.page(page)
        except PageNotAnInteger:
            shop_list = pagination.page(1)
        except EmptyPage:
            raise Http404("That page contains no results")

        context['shops'] = shop_list.object_list
        context['country_id'] = self.request.GET.get('country')
        context['page_obj'] = shop_list

        return context


class FaqView(ListView):
    template_name = 'sections/FAQ.html'
    queryset = FaqBlock.objects.all()

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
