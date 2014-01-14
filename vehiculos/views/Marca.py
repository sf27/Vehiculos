from vehiculos.models import Marca
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone


class MarcaDetailView(DetailView):

    queryset = Marca.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(MarcaDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object

class MarcaCreate(CreateView):
    model = Marca
    success_url = reverse_lazy('marcas_registradas')

class MarcaUpdate(UpdateView):
    model = Marca
    success_url = reverse_lazy('marcas_registradas')

class MarcaDelete(DeleteView):
    model = Marca
    success_url = reverse_lazy('marcas_registradas')

class MarcaListView(ListView):
    model = Marca
    template_name = 'marca_list.html'
    paginate_by = 10  #and that's it !!