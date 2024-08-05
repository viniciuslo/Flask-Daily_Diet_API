Daily Diet API
# Descrição

A Daily Diet API é uma aplicação construída em Flask para gerenciar a dieta diária dos usuários. Ela permite criar, atualizar, deletar e listar refeições. A documentação da API é disponibilizada via Swagger-UI.

## Estrutura do Projeto

```

daily_diet_api/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│
├── instance/
│   └── daily_diet.db
│
├── static/
│   └── swagger.yaml
│
├── requirements.txt
├── run.py
```

## Requisitos

- Python 3.12+
- Flask 2.3.2
- Flask-SQLAlchemy 3.0.3
- Flask-Swagger-UI 4.11.1

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/viniciuslo/Flask-Daily_Diet_API.git
cd daily_diet_api
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
# venv\Scripts\activate  # Para Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie o banco de dados:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

## Uso

1. Inicie a aplicação:

```bash
python run.py
```

2. Acesse a documentação da API no Swagger-UI:

Abra o navegador e acesse http://localhost:5000/swagger.

## Endpoints

### Criar uma nova refeição

- URL: /meals
- Método: POST
- Corpo da Requisição:

```json
{
    "name": "Salada",
    "description": "Salada verde com tomate",
    "date_time": "2024-08-05T12:30:00",
    "in_diet": true,
    "user_id": 1
}
```

### Listar todas as refeições

- URL: /meals
- Método: GET

### Obter uma refeição específica

- URL: /meals/{id}
- Método: GET

### Atualizar uma refeição

- URL: /meals/{id}
- Método: PUT
- Corpo da Requisição:

```json
{
    "name": "Salada Atualizada",
    "description": "Salada verde com tomate e cenoura",
    "date_time": "2024-08-06T12:30:00",
    "in_diet": false
}
```

### Deletar uma refeição

- URL: /meals/{id}
- Método: DELETE

## Licença

Este projeto está licenciado sob a MIT License.
