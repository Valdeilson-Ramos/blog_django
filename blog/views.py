from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone

#View que gera a listagem de post na tela inicial
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

#View que Mostra o Post individual de acordo com o id recebido: pk
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post}) 

#View que insere um novo Post através do formulário
def post_new(request):
     if request.method == "POST": #verificando se há uma solicitação de envio de dados pelo metodo POST do formulário (fomulario preenchido)
         form = PostForm(request.POST) #Se houver requisiução, o form recebe os dados enviados do formulário
         if form.is_valid():           #Verifica se os dados são válidos e estão preenchidos
             post = form.save(commit=False) #Não salva os dados ainda para inserir o autor e data de publicação que não vem via formulário
             post.author = request.user    #Pega o usuário logado
             post.published_date = timezone.now() #Insere a data atual
             post.save()                          #Salva o fomulário
             return redirect('post_detail', pk=post.pk) #Retorna a view que mostra o post detalhado
     else:
         form = PostForm()     #Chama o formulário em branco
     return render(request, 'blog/post_edit.html', {'form': form}) #mostra formulário em branco

def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'blog/post_edit.html', {'form': form})