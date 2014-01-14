from vehiculos.models import Vehiculo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone


class VehiculoDetailView(DetailView):

    queryset = Vehiculo.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(VehiculoDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object

class VehiculoCreate(CreateView):
    model = Vehiculo
    success_url = reverse_lazy('vehiculos_registrados')

class VehiculoUpdate(UpdateView):
    model = Vehiculo
    success_url = reverse_lazy('vehiculos_registrados')

class VehiculoDelete(DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('vehiculos_registrados')

class VehiculoListView(ListView):
    model = Vehiculo      # shorthand for setting queryset = models.Car.objects.all()
    template_name = 'vehiculo_list.html'  # optional (the default is app_name/modelNameInLowerCase_list.html; which will look into your templates folder for that path and file)
    paginate_by = 10  #and that's it !!