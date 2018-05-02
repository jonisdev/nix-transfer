Python 3.6.3 | Django 2.0.4 | Django Rest Framework 2.2.0

## Banco Nix Transferencias

Esta API oferece a possibilidade de realizar trasações de transferencias para
um usuário com CNPJ que esteja cadastrado.


#### Para rodar localmente 

```
$ git clone https://github.com/jonatanvianna/nix-transfer.git

$ cd nix-transfer

$ python -m venv my_env

$ source my_env/bin/activate

$ pip install -r requirements.txt

$ python manage.py test

$ python manage.py runserver

```

### Documentação 
Para verificar os endpoints disponíveis, acesse:
```
http://127.0.0.1:8000/swagger/
```

### Filtros
Para filtrar é possível usar os seguintes filtros

```
http://127.0.0.1:8000/api/v1/transfers/?payer_name=Marie Curie
http://127.0.0.1:8000/api/v1/transfers/?beneficiary_name=Marie Curie
```
É possivel usar também a Browseable API nativa do Django Rest Framework em:
```http://127.0.0.1:8000/api/v1/transfers/```

