
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def inicio(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            access = authenticate(username=usuario, password=clave)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    #request.session['usuario'] = usuario
                    return HttpResponseRedirect('/')
                else:
                    return render_to_response('no_activo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('no_usuario.html', context_instance=RequestContext(request))
    else:
        form = AuthenticationForm()
    return render_to_response('inicio.html', {'formulario': form}, context_instance=RequestContext(request))


@login_required(login_url='/inicio')
def privado(request):
    usuario = request.user
    return render_to_response('index.html', {'usuario': usuario}, context_instance=RequestContext(request))

@login_required(login_url='/inicio')
def cerrar_sesion(request):
    logout(request)
    #if request.session.has_key('usuario'):
    #    del request.session['usuario']
    return HttpResponseRedirect('/inicio')
