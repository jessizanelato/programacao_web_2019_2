from django.shortcuts import render, redirect
from .models import TodoList, Category

def index(request): # index view
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