from django.shortcuts import render
from .models import Funcionario

def index(request):

    #primeiro buscamos os funcionarios

    funcionarios = Funcionario.objetos.all()

    #incluimos no contexto
    context = {
        'funcionarios': funcionarios
    }

    #retornamos o template para listagem de funcionarios
    return render(
        request,
        "index.html",
        context
    )

