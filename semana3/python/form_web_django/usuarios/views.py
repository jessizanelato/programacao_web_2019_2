from django.shortcuts import render
from django.core.validators import validate_email

from html import escape

def preprocessa(campo):
    if campo is not None:
        return escape(bytes(campo.strip(), "utf-8").decode("unicode_escape"))
    else:
        return ""

def usuario_criar(request):
    contexto = {}    
    
    if request.method == "POST":
        contexto = {
            "campos": {
                "nome": preprocessa(request.POST.get("nome")),
                "email": preprocessa(request.POST.get("email")),
                "senha": preprocessa(request.POST.get("senha")),
                "conf_senha": preprocessa(request.POST.get("conf_senha")),
                "cidade": preprocessa(request.POST.get("cidade")),
                "idade": preprocessa(request.POST.get("idade")),
                "comentarios": preprocessa(request.POST.get("comentarios")),
                "sexo": preprocessa(request.POST.get("sexo")),
                "termos": preprocessa(request.POST.get("termos"))
            }
        }
        contexto['erros'] = validate_usuario_criar(contexto['campos'])
    return render(request, "usuario_criar.html", contexto)

def validate_usuario_criar(campos):
    erros = []
    if not campos['nome']:
        erros.append("Nome é campo obrigatório.")
    if not campos['email']:
        erros.append("E-mail é campo obrigatório.")
    else:
        try:
            validate_email(campos['email'])
        except:
            erros.append("E-mail inválido.")    
    if not campos['senha']:
        erros.append("Senha é campo obrigatório.")
    if not campos['conf_senha']:
        erros.append("Confirmar senha é campo obrigatório.")
    elif campos['conf_senha'] != campos['senha']:
        erros.append("Senhas não conferem.")
    if campos['idade'] and not campos['idade'].isdigit():
        erros.append("Idade deve ser um inteiro maior ou igual a 0.")
    if not campos['termos']:
        erros.append("Você precisa concordar com os termos de uso.")
    return erros