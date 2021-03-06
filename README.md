# API-cadastroAluno

![](images/django-rest-framework.png)

Nesta api está sendo utilizada os frameworks e linguagens abaixo:
- Django Rest Framework
- Python

**Iniciar api**

```python
    source venv/bin/activate
    python manage.py runserver
```

**Migração**

Primeiramente gere o arquivo de migração com o comando abaixo

```python
    python manage.py makemigrations
```

Após executar o comando acima, verifique se não ocorreu erros e execute o seguinte que fará a imigração de dados para o banco local.

```python
    python manage.py migrate
```


**Paramêtros:** _(request body)_


| Paramêtros |  Tipo  |     Descrição      |
|------------|--------|--------------------|
| id         | number | Id do aluno        |
| first_name | str    | Primeiro nome      |
| last_name  | str    | Sobrenome          |
| cpf        | number | Número de CPF      |
| number     | number | Número de telefone |
| email      | str    | Email              |

**Resposta:**

```javascript
{
    "id": 1,
    "first_name": Mayara,
    "last_name": Matos,
    "cpf": 99988877766,
    "number": 14981374505,
    "email": may@gmail.com,
}
```

**Endpoints:**
> http://127.0.0.1:8000/student-registration/
> 
> http://127.0.0.1:8000/student-registration/1/
