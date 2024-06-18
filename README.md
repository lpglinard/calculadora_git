# Calculadora FastAPI

## Descrição
Este projeto implementa uma calculadora simples utilizando FastAPI, um framework moderno e rápido para a construção de APIs em Python 3.7+. A API permite realizar operações matemáticas básicas como adição, subtração, multiplicação e divisão.

## Requisitos
- Python 3.7+
- FastAPI
- Uvicorn (servidor ASGI)

## Instalação

Antes de começar, certifique-se de ter o Python 3.7 ou superior instalado. Também será necessário o pip para instalar as dependências.

### Passos para instalação:

1. Clone o repositório:
   ```bash
   git clone https://seu-repositorio/calculadora-fastapi.git
   cd calculadora-fastapi

# Uso da API

A API possui endpoints para realizar as quatro operações matemáticas básicas. Você pode acessar os seguintes endpoints:

    Adição: /add/?num1=<num1>&num2=<num2>
    Subtração: /subtract/?num1=<num1>&num2=<num2>
    Multiplicação: /multiply/?num1=<num1>&num2=<num2>
    Divisão: /divide/?num1=<num1>&num2=<num2>

# Exemplos de uso
## Adição
`curl -X 'GET' 'http://127.0.0.1:8000/add/?num1=10&num2=5' -H 'accept: application/json'
`