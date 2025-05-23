# Python_BackEnd_API_Request

Este projeto faz parte do meu portfólio pessoal de desenvolvimento em Python, com foco na construção de soluções Back-End modernas e performáticas.

## 🎯 Objetivo

Criar uma aplicação Back-End utilizando **FastAPI** que:

- Integra com uma API externa (consumo de dados via HTTP)
- Realiza o tratamento, transformação e validação dos dados recebidos
- Disponibiliza os dados de forma estruturada e segura para consumo por aplicações Front-End

## 🚀 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) — servidor ASGI
- [Requests](https://docs.python-requests.org/)
- [Pydantic](https://docs.pydantic.dev/) — para validação de dados
- [Pytest](https://docs.pytest.org/) — para testes automatizados (opcional)

## 📁 Estrutura do Projeto

```
Python_BackEnd_API_Request/
├── src/
│   ├── data/             # Rotas e endpoints
│   ├── domain/          # Integrações com APIs externas
│   ├── errors/          # Modelos e validações com Pydantic
│   ├── util/            # Configurações e Consumers
│   └── main/            # Aplicação
├── tests/               # Testes automatizados
├── requirements.txt     # Dependências do projeto
└── README.md
```

## ▶️ Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/camaral2/Python_BackEnd_API_Request.git
   cd Python_BackEnd_API_Request
   ```

2. Crie um ambiente virtual e ative:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o servidor FastAPI:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Acesse a documentação interativa:
   - Swagger: [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)
   - Redoc: [http://127.0.0.1:8001/redoc](http://127.0.0.1:8001/redoc)

## 📌 Notas

- Este projeto será evoluído com autenticação, paginação, testes automatizados e integração com banco de dados.
- Serve como base para novos projetos Back-End usando FastAPI.

---

🧑‍💻 *Desenvolvido por Cristian Amaral — entusiasta de Python e soluções Back-End.*
