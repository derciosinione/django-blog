from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PerfilUpdateForm, UserRegisterForm, UserUpdateForm
from django.contrib import messages

# Registar Usuário.
def register(request):
    """
    Registar Usuário.
    """
    if request.method=='POST':
        # Formulario de registar usuario
        form = UserRegisterForm(request.POST)
        # Validar o formulario de registar usuario
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            messages.success(request,f'A sua conta foi criada, agora podes fazer o login.')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    
    return render(request,'users/register.html',{'form':form})

@login_required
def perfil(request):
    if request.method=='POST':
        form_user = UserUpdateForm(request.POST, instance=request.user)
        form_perfil = PerfilUpdateForm(request.POST, request.FILES , instance=request.user.perfil)

        #Verificar se os formulários são válidos 
        if form_user.is_valid() and form_perfil.is_valid():
            form_user.save()
            form_perfil.save()
            messages.success(request,f'Perfil actualizado com sucesso.')
            return redirect('users:perfil')
    else:
        form_user = UserUpdateForm(instance=request.user)
        form_perfil = PerfilUpdateForm(instance=request.user.perfil)
        
    context = {
        'form_user': form_user,
        'form_perfil': form_perfil,
        'title': 'Perfil',
    }
    return render(request,'users/perfil.html',context)