## Criação de Sistema Web da empresa Eletrooliveira

Criacao do sistema:

Instalação do python 3.13.12

Criaçao de ambiente virtual venv

```Python -m venv venv ``` comando que cria o ambiente venv na pasta venv

Abrindo ambiente virtual no terminal
```./venv/Scripts/activate ```

Instalando o django através do pip pelo terminal
```pip install django```


Criação do projeto eletrooliveira utilizando django

```manage.py startproject eletrooliveira```

Criação do app dentro da pasta do projeto

```manage.py startapp core```

Criação da pasta templates na raiz do projeto

Criação de index.html "Hello World!"
```<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Eletro Oliveira</title>
</head>
<body>
<h1>Bem vindo a página Eletro Oliveira</h1>
</body>
</html>```
```
Criação da View dentro do arquivo views.py que só retorna o html criado acima

```
def index_eletro(request):
    return render(request,'index.html')
```

Adição da path dentro o arquivo urls.py

```
path('index/',views.index_eletro),
```

Criação do banco de dados MYSQL no Workbench
```
Conexão: localhost
usuário: root
senha: 1234
```
Configuração do Banco de Dados no settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dboliveira',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST':'localhost',
        'PORT': 3306,
    }
}
```
Mudança na configuração da linguagem para pt-BR e horário na settings.py
```aiignore
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```
Criação da tabela no banco de dados através do models.py

```aiignore
class Dados_orcamento(models.Model):
    nome_cliente = models.CharField(max_length=100)
    endereco_logradouro = models.CharField(max_length=100)
    endereco_numero = models.IntegerField()
    endereco_cidade = models.CharField(max_length=40)
    endereco_estado = models.CharField(max_length=2)
    tipo_imovel = models.CharField(max_length=20)
    consumo_energia = models.IntegerField(blank=True, null=True)
    imagem = models.FileField(upload_to='images/orcamento', default=None, null=True, blank=True)
    data_inicial_orcamento = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, default='aguardando' )

    class Meta:
        db_table = 'orcamento'

    def __str__(self):
        return self.nome_cliente

```

Inserção das rotas para o armazenamento do arquivo no settings.py

```aiignore
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'public')
```

Concatenacao das rotas com a a rota estática do urls.py

```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
Criada apresentação para manipulação do banco de dados no perfil administrador no admin.py

```
from django.contrib import admin
from core.models import Dados_orcamento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente','data_inicial_orcamento')

admin.site.register(Dados_orcamento, EventoAdmin)
```
