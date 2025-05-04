# ChatBot FURIA para Fãs de CS:GO

Este é um chat interativo para fãs da FURIA, criado com Flask e HTML. Com uma interface simples e acessível, o bot simula interações com a torcida e oferece links úteis para acompanhar o time.

## Funcionalidades

- Simula uma conversa com o "Bot da FURIA"
- Respostas automáticas baseadas em botões (Jogadores, Produtos, Jogos, etc)
- Links diretos para redes sociais, loja, suporte e partidas
- Interface estilizada com a identidade visual da FURIA

## Como rodar localmente

### Requisitos

- Python 3
- `pip` instalado

### Passos

1. Clone o repositório:

git clone https://github.com/seu-usuario/furia-chatbot.git
cd furia-chatbot

2. Instale as dependências:

pip install -r requirements.txt

3. Inicie o servidor Flask:

python app.py

4. Acesse no navegador:

http://127.0.0.1:5000/ (Se rodado no code space entre no link gerado pelo proprio git)

Estrutura do Projeto

├── app.py
├── views.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── requirements.txt
└── README.md