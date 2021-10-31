from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import FormView

from parcels.forms import EditForm, AddForm
from parcels.models import Parcel


class ParcelListView(LoginRequiredMixin, FormView):
    template_name = 'parcels/parcels.html'
    login_url = '/sign/'
    paginate_by = 2
    form_class = EditForm

    def get_queryset(self):
        return self.request.user.parcels.filter(is_deleted=False).order_by('id')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        pagination = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get('page')

        try:
            page_obj = pagination.page(page)
        except PageNotAnInteger:
            page_obj = pagination.page(1)
        except EmptyPage:
            raise Http404("That page contains no results")

        context['page_obj'] = page_obj
        context['object_list'] = page_obj.object_list
        return context

    def post(self, request, *args, **kwargs):
        # delete
        if 'delete' in request.POST:
            parcel_id = request.POST['delete']
            parcel = get_object_or_404(Parcel, pk=parcel_id)
            parcel.is_deleted = True
            parcel.save()
            return self.render_to_response(self.get_context_data())

        # create
        if 'track' in request.POST:
            track = request.POST.get('track')
            if Parcel.objects.filter(track=track).exists():
                return JsonResponse({'data': False}, status=450)
            else:
                form = AddForm(request.POST)
                parcel = form.save(commit=False)
                parcel.user = self.request.user
                parcel.save()
                return JsonResponse({'data': True}, status=200)

        # get parcels data to edit
        if 'edit' in request.POST:
            parcel_id = request.POST.get('edit')
            parcel = get_object_or_404(Parcel, pk=parcel_id)
            edit_form = EditForm(instance=parcel)
            self.template_name = 'parcels/edit-form.html'

            return self.render_to_response(
                self.get_context_data(edit_form=edit_form,
                                      parcel_track=parcel.track),
                status=201)

        if 'price' not in request.POST:
            form = EditForm(request.POST)
            if form.is_valid():

                data = form.cleaned_data
                parcel_id = data['id']
                parcel = get_object_or_404(Parcel, pk=parcel_id)
                parcel.name = data['name']
                parcel.type = data['type']
                parcel.store = data['store']
                parcel.site = data['site']
                parcel.comment = data['comment']
                parcel.save()

                return HttpResponse(status=201)
            else:
                self.template_name = 'parcels/edit-form.html'
                return self.render_to_response(self.get_context_data(edit_form=form))








