# ClientServerBasics (2.0)

# Calculadora Remota - Cliente e Servidor com Sockets

## Descrição

Esta aplicação é uma **calculadora remota** implementada com **sockets**. Ela permite que um cliente envie operações matemáticas para um servidor, que executa a operação e retorna o resultado. O cliente pode enviar operações como soma, subtração, multiplicação e divisão, e o servidor irá calcular e enviar a resposta de volta ao cliente.

## Funcionalidades

- **Operações suportadas:**

  - Soma: `add a b c ... z`
  - Subtração: `subtract a b c ... z`
  - Multiplicação: `multiply a b c ... z`
  - Divisão: `divide a b c ... z`

- **Fluxo de interação:**
  - O cliente se conecta ao servidor.
  - O cliente envia uma operação matemática ao servidor.
  - O servidor executa a operação e retorna o resultado.
  - O cliente pode continuar enviando operações ou digitar "exit" para encerrar a comunicação.

---

## Arquitetura

A aplicação consiste em dois componentes principais:

### 1. Servidor (`server.py`)

O servidor aguarda a conexão de um cliente, recebe os dados (operações matemáticas) e executa as operações. Ele suporta as operações de soma, subtração, multiplicação e divisão.

**Características principais:**

- O servidor escuta conexões na porta configurada.
- Ao receber uma operação, ele processa os dados e retorna o resultado.
- O servidor usa **TCP (SOCK_STREAM)** para comunicação.
- Suporte a múltiplos clientes utilizando threads, se necessário.

### 2. Cliente (`client.py`)

O cliente é responsável por se conectar ao servidor e enviar as operações matemáticas. O cliente permite que o usuário insira comandos como “add”, “subtract”, “multiply”, e “divide”, e também pode digitar “exit” para encerrar a conexão.

**Características principais:**

- O cliente envia operações matemáticas ao servidor.
- Após o envio da operação, o cliente recebe a resposta e a exibe.
- O cliente pode continuar enviando operações até que o usuário digite “exit”.
- Comunicação via **TCP** com o servidor.
  > > > > > > > 1418ac7 (Add client-server calculator implementation with threading support)
