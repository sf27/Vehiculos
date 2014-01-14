from vehiculos.models import Institucion
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone


class InstitucionDetailView(DetailView):

    queryset = Institucion.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(InstitucionDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object

class InstitucionCreate(CreateView):
    model = Institucion
    success_url = reverse_lazy('instituciones_registradas')

class InstitucionUpdate(UpdateView):
    model = Institucion
    success_url = reverse_lazy('instituciones_registradas')

class InstitucionDelete(DeleteView):
    model = Institucion
    success_url = reverse_lazy('instituciones_registradas')

class InstitucionListView(ListView):
    model = Institucion
    template_name = 'institucion_list.html'
    paginate_by = 10