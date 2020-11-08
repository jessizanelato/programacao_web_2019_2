from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout #importação dos métodos utilizados para ver o login/logout e autenticação

from .models import TodoList, Category

def do_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) #método para verificar se a senha está correta
        if user is not None:
            login(request, user)
            return redirect("/") # redireciona para a página principal
        else:
            return redirect('/login?erro=true')
    else:
        mensagem_erro = 'Usuário e/ou senha não conferem.' if 'erro' in request.GET else ''
    return render(request, 'login.html', {'mensagem_erro': mensagem_erro})

def do_logout(request):
    logout(request)
    return redirect('/login') #redireciona para a página de login novamente

def index(request): # index view
    if not request.user.is_authenticated:
        return redirect('/login')

    todos = TodoList.objects.all() # buscando todos os todos com o object manager
    categories = Category.objects.all() # buscando todas as categorias com o object manager    
    if request.method == "POST": # checando se o metodo request é POST
        if "taskAdd" in request.POST: # checando se a requisição é para adicionar um todo
            title = request.POST["description"] # titulo
            date = str(request.POST["date"]) # data
            category = request.POST["category_select"] # categoria
            content = title + " -- " + date + " " + category # conteúdo
            # criando um novo todo list para salvar no banco
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(id=category))
            Todo.save() # salvando
            return redirect("/") # recarregando a página após o sucesso
        if "taskDelete" in request.POST: # checando se a requisição é para deletar um todo
            checkedlist = request.POST["checkedbox"] # pegando os ids a serem deletados
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) # buscando pelo id do todolist      
                todo.delete() # deletando o todo

    return render(request, "index.html", {"todos": todos, "categories":categories}) # renderizando na página os todos e categorias