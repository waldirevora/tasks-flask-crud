# 📋 Tasks Flask CRUD

API RESTful para gerenciamento de tarefas (_CRUD_), desenvolvida em Python utilizando o microframework **Flask**. Este projeto foi construído como parte do módulo prático do curso de Python da **Rocketseat**.

---

## 🚀 Funcionalidades

- **`POST /tasks`**: Cria uma nova tarefa.
- **`GET /tasks`**: Lista todas as tarefas cadastradas com totalizador.
- **`GET /tasks/<id>`**: Obtém os detalhes de uma tarefa específica.
- **`PUT /tasks/<id>`**: Atualiza título, descrição e status de conclusão da tarefa.
- **`DELETE /tasks/<id>`**: Remove uma tarefa.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Flask** (Microframework Web)
- **Pytest** & **Requests** (Testes de integração automatizados)

---

## 📦 Como Executar o Projeto

### Pré-requisitos

- Python 3.10+ instalado.
- Git instalado.

### 1. Clonar o Repositório

```bash
git clone [https://github.com/waldirevora/tasks-flask-crud.git](https://github.com/waldirevora/tasks-flask-crud.git)
cd tasks-flask-crud

```

### 2. Criar e Ativar o Ambiente Virtual (Recomendado)

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate

```

### 3. Instalar as Dependências

```bash
pip install flask pytest requests

```

### 4. Executar a Aplicação

```bash
python app.py

```

A API estará rodando em: `http://127.0.0.1:5000`

---

## 🧪 Executando os Testes Automatizados

Com a API rodando em um terminal, abra um segundo terminal e execute o conjunto de testes com o `pytest`:

```bash
python -m pytest .\tests.py -v

```

---

## 🎓 Créditos

Projeto desenvolvido para fins de aprendizado durante o curso da **Rocketseat**.

```

```
