# Projeto Python - Sistema de Cadastro e Suporte

## Descrição

Este projeto é um sistema desenvolvido em Python, com funcionalidades de cadastro e suporte, utilizando uma arquitetura cliente-servidor. O sistema oferece uma interface gráfica para interação com o usuário, permitindo cadastrar informações e fornecer suporte. A interface foi construída utilizando a biblioteca Qt, com telas de cadastro, menu e outras funcionalidades interativas.


O sistema é dividido em duas partes principais:

- **Cliente**: Responsável por interagir com o servidor e enviar dados para cadastro ou consulta.
- **Servidor**: Processa as requisições do cliente, realizando operações de cadastro e gerenciando a comunicação entre o cliente e o banco de dados.

Além disso, o projeto conta com uma série de telas gráficas para facilitar a interação do usuário com o sistema.

## 🚀 Funcionalidades

- **Cliente**: Interage com o servidor e faz requisições para o sistema de cadastro.
- **Servidor**: Gerencia as requisições e processa os dados de cadastro e suporte.
- **Interface Gráfica**: Tela de cadastro, menu principal e outras funcionalidades de suporte.
- **Banco de Dados**: Conexão com banco de dados para armazenar informações de usuários.

## 📁 Estrutura do Projeto
```bash
Projeto-pythonn/
├── 📁 Codigo-python/
│   ├── 📁 Cliente/
│   │   └── 📄 cliente.py  # Código do cliente que interage com o servidor
│   └── 📁 Servidor/
│       ├── 📄 cadastro.py  # Código para gerenciar cadastros
│       ├── 📄 conexao.py   # Gerencia a conexão do servidor
│       └── 📄 servidor.py  # Código principal do servidor
├── 📁 Imagens/
│   ├── 📄 logo-simbolo.png  # Imagem do logo
│   ├── 📄 logo-versao-completa.png  # Imagem do logo com versão completa
│   └── 📄 logo-versao_completa-removebg-preview.png  # Imagem do logo
├── 📁 Sobre o projeto/
│   └── 📄 README.md  # Documentação detalhada sobre o projeto
├── 📁 TelasUi/
│   ├── 📄 suporte.ui  # Tela de suporte
│   ├── 📄 cadastro1.ui  # Tela de cadastro
│   ├── 📄 ideais.ui  # Tela de ideias
│   ├── 📄 menu1.ui  # Tela do menu principal
│   ├── 📄 prepesquisa.ui  # Tela de pesquisa
│   ├── 📄 simbolo.qrc  # Arquivo de recursos do Qt
│   ├── 📄 sobrenos.ui  # Tela "Sobre nós"
│   ├── 📄 tela.qrc  # Arquivo de recursos Qt
│   ├── 📄 tela1.ui  # Outra tela da interface
│   └── 📄 vacina.ui  # Tela de vacina
├── 📁 __pycache__/  # Cache dos arquivos Python compilados
│   ├── 📄 cadastro.cpython-310.pyc
│   ├── 📄 cliente.cpython-310.pyc
│   ├── 📄 conexao.cpython-310.pyc
│   └── 📄 tela_ideias.cpython-310.pyc
├── 📄 LICENSE  # Arquivo de licença
├── 📄 README.md  # Documentação do projeto
└── 📁 .git/  # Diretório do repositório Git

```


## 📌 Requisitos

- **Python 3.x**
- **PyQt5** para criação da interface gráfica
- **Bibliotecas adicionais** que podem ser instaladas via `requirements.txt` (se disponível).

## ▶️ Como Rodar

### 1. Clone o repositório

```bash
git clone https://github.com/usuario/Projeto-pythonn.git
cd Projeto-pythonn
```
### 2. Instale as dependências
```bash
pip install -r requirements.txt
```
### 3. Execute o Servidor
```bash
python Codigo-python/Servidor/servidor.py

```
### 4. Execute o Cliente
```bash
python Codigo-python/Cliente/cliente.py

```
