# Web DentiCare Odontologia (Versão PT-BR)

Este repositório contém o código fonte do **Web DentiCare Odontologia**, uma aplicação web completa para clínicas odontológicas, totalmente traduzida e adaptada para o Português.

O sistema permite a gestão de serviços, venda de produtos odontológicos, agendamento de consultas (via contato), gerenciamento de usuários e pedidos.

## 📋 Funcionalidades Principais

*   **Página Inicial (`Inicio`)**: Apresentação da clínica e destaques.
*   **Catálogo de Serviços (`Servicos`)**: Listagem dos tratamentos e serviços oferecidos.
*   **Loja de Produtos (`Produtos`)**: Catálogo de produtos para higiene e cuidados bucais.
*   **Carrinho de Compras (`Carrinho`)**: Funcionalidade completa de adicionar, remover e atualizar quantidades de itens.
*   **Gestão de Pedidos (`Pedido`)**: Processamento de ordens de compra realizadas pelos clientes.
*   **Autenticação de Usuários (`Autenticacao`)**: Registro, login e logout de clientes.
*   **Contato (`Contato`)**: Formulário para dúvidas e pré-agendamentos.
*   **Painel Administrativo**: Interface poderosa para gestão de todo o conteúdo do site.

## 🛠️ Tecnologias Utilizadas

*   **Backend**: Python, Django Framework
*   **Banco de Dados**: PostgreSQL
*   **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
*   **Gerenciamento de Arquivos Estáticos**: WhiteNoise
*   **Deploy**: Configurado para Render (com `build.sh`)

---

## 🚀 Como Rodar o Projeto Localmente

Siga estes passos para configurar o ambiente de desenvolvimento na sua máquina.

### 1. Pré-requisitos
Certifique-se de ter o **Python 3.10+** e o **Git** instalados.

### 2. Clonar o Repositório

```bash
git clone https://github.com/DomHenrique/web-denticare-odontologia-pt.git
cd web-denticare-odontologia-pt
```

### 3. Criar e Ativar Ambiente Virtual

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 4. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto (baseado em algum exemplo ou solicite as chaves ao responsável) com as seguintes variáveis (exemplo):

```env
SECRET_KEY='sua-chave-secreta-django'
DEBUG=True
DATABASE_URL='postgres://usuario:senha@localhost:5432/nome_banco'
EMAIL_HOST_USER='seu-email@gmail.com'
EMAIL_HOST_PASSWORD='sua-senha-de-app'
```

### 6. Aplicar Migrações (Banco de Dados)
Isso criará as tabelas necessárias no seu banco de dados.

```bash
python manage.py migrate
```

### 7. Criar um Superusuário (Administrador)
Para acessar o painel administrativo, você precisa de uma conta admin.

```bash
python manage.py createsuperuser
```
Siga as instruções para definir nome de usuário, email e senha.

### 8. Iniciar o Servidor
```bash
python manage.py runserver
```
Acesse o site em: `http://127.0.0.1:8000/`

---

## 🔐 Guia do Administrador (Painel Admin)

O sistema possui uma área restrita para gerenciamento. Para acessar, vá para:
**`http://127.0.0.1:8000/admin/`** e faça login com seu superusuário.

Aqui está o passo a passo para gerenciar cada seção:

### 1. Gerenciar Produtos (`Produtos`)
Para adicionar novos produtos à loja:
1.  No painel, procure pela seção **Produtos**.
2.  Clique em **Categorias** para criar tipos de produtos (ex: "Escovas", "Cremes Dentais").
    *   Clique em "Adicionar Categoria", dê um nome e salve.
3.  Clique em **Produtos** para cadastrar o item.
    *   **Nome**: Nome do produto.
    *   **Categorias**: Selecione a categoria criada anteriormente.
    *   **Imagem**: Faça upload da foto do produto.
    *   **Preço**: Defina o valor.
    *   **Disponibilidade**: Marque se está disponível para venda.

### 2. Gerenciar Serviços (`Serviços`)
Para listar os tratamentos que a clínica oferece:
1.  Vá até a seção **Serviços**.
2.  Clique em **Serviços** > **Adicionar serviço**.
3.  Preencha:
    *   **Título**: Nome do serviço (ex: "Clareamento Dental").
    *   **Conteúdo**: Breve descrição.
    *   **Imagem**: Imagem ilustrativa.

### 3. Gerenciar Pedidos (`Pedidos`)
Quando um cliente finaliza uma compra, um pedido é criado aqui.
1.  Vá até a seção **Pedidos**.
2.  Clique em **Pedidos** para ver a lista de compras.
3.  Você pode ver quem comprou (`User`), o status e o total.
4.  Para ver os itens de um pedido específico, vá em **Item de Pedidos**.

### 4. Gerenciar Usuários
Você pode visualizar, editar ou remover clientes cadastrados na seção **Auth** > **Users**.

---

## 📦 Estrutura do Projeto

*   `Autenticacao/`: Gerencia login e registro.
*   `Carrinho/`: Lógica do carrinho de compras (sessão).
*   `Contato/`: Formulário de contato e envio de e-mails.
*   `Inicio/`: Página principal e templates base.
*   `Pedido/`: Processamento e registro de pedidos no banco.
*   `Produtos/`: Modelos de Categoria e Produto.
*   `Servicos/`: Modelos e views para serviços odontológicos.
*   `DentiCareWeb/`: Configurações principais projeto (`settings.py`, `urls.py`).
*   `manage.py`: Utilitário de linha de comando do Django.

## ☁️ Deploy (Produção)

Este projeto contém um arquivo `build.sh` configurado para deploys automatizados em plataformas como o **Render**.

**Comanado de Build:**
```bash
./build.sh
```
Este script instala as dependências, roda as migrações e coleta os arquivos estáticos.

**Configuração do WhiteNoise:**
Os arquivos estáticos (CSS, JS, Imagens) são servidos de forma eficiente usando a biblioteca WhiteNoise, conforme configurado em `settings.py`.
