# QWEN.md - Web DentiCare Odontologia

## Project Overview

**Web DentiCare Odontologia** is a complete web application for dental clinic management, built with **Django 6.0** and **Python 3.13**. The system is fully localized in **Portuguese (PT-BR)** and provides:

- **Home Page (`Inicio`)**: Clinic presentation and highlights
- **Services Catalog (`Servicos`)**: Listing of dental treatments and services
- **Product Store (`Produtos`)**: Catalog of oral hygiene and care products with shopping cart
- **Shopping Cart (`Carrinho`)**: Add, remove, and update product quantities
- **Order Management (`Pedido`)**: Processing and tracking of customer orders
- **User Authentication (`Autenticacao`)**: Customer registration, login, and logout
- **Contact (`Contato`)**: Contact form for inquiries and pre-scheduling
- **Appointment Scheduling (`Agendamento`)**: Professional scheduling with availability management
- **Company Units (`Empresa`)**: Management of clinic locations/branches
- **Admin Panel**: Customized Django admin with Jazzmin theme

### Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.13, Django 6.0 |
| **Database** | PostgreSQL (via `psycopg`), also supports MySQL (`PyMySQL`) |
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5 |
| **Admin Theme** | django-jazzmin |
| **Static Files** | WhiteNoise |
| **Deployment** | Gunicorn, Docker, Render-ready (`build.sh`) |
| **Forms** | django-bootstrap5, django-crispy-forms, django-widget-tweaks |

---

## Project Structure

```
web-denticare-odontologia/
├── DentiCareWeb/          # Main Django settings, urls, wsgi
│   ├── settings.py        # Project configuration (DB, email, static, etc.)
│   └── urls.py            # Root URL routing
├── Inicio/                # Home page app
├── Servicos/              # Dental services catalog
├── Produtos/              # Product catalog (Categoria, Produto models)
├── Carrinho/              # Shopping cart logic (session-based)
├── Pedido/                # Order processing (Pedido, ItemPedido models)
├── Autenticacao/          # User registration/login
├── Contato/               # Contact form and email
├── Agendamento/           # Appointment scheduling (Profissional, Disponibilidade, Agendamento)
├── Empresa/               # Clinic unit management (Unidade model)
├── media/                 # Uploaded media files
├── staticfiles/           # Collected static assets
├── manage.py              # Django CLI utility
├── requirements.txt       # Python dependencies
├── docker-compose.yml     # Docker setup (PostgreSQL + web)
├── Dockerfile             # Container configuration
└── build.sh               # Build script for Render deployment
```

---

## Key Models

### Produtos
- **Categoria**: nome, imagem, criado, atualizado
- **Produto**: nome, categorias (FK), sku, preco, marca, codigo_interno, apresentacao, descricao, imagem_produto, disponibilidade, estoque

### Servicos
- **Servico**: titulo, conteudo, imagem

### Pedido
- **Pedido**: user (FK), criado_em, total (property)
- **ItemPedido**: user (FK), produto (FK), pedido (FK), quantidade

### Agendamento
- **Profissional**: nome, especialidade, foto, servicos (M2M)
- **Disponibilidade**: profissional (FK), dia_semana, hora_inicio, hora_fim, intervalo
- **Agendamento**: servico (FK), profissional (FK), data, horario, nome_cliente, telefone, observacoes, status

### Empresa
- **Unidade**: nome, tipo (matriz/filial), endereco, cidade, estado, email, telefone, whatsapp, mapa_url, ordem

---

## Building and Running

### Local Development

```bash
# 1. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file with required variables:
#    SECRET_KEY, DEBUG, DATABASE_URL, EMAIL_HOST_PASSWORD

# 4. Run migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Start development server
python manage.py runserver
```

Access at: `http://127.0.0.1:8000/`
Admin panel: `http://127.0.0.1:8000/admin/`

### Docker

```bash
docker-compose up --build
```

This starts PostgreSQL (port 5435) and the web app (port 8000).

### Production Build (Render)

```bash
./build.sh
```

The script installs dependencies, collects static files, and applies migrations.

### Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Debug mode (True/False) |
| `DATABASE_URL` | Database connection string |
| `EMAIL_HOST_PASSWORD` | SMTP password for email |
| `RENDER_EXTERNAL_HOSTNAME` | Auto-set by Render |

---

## Development Conventions

- **Language**: Code comments and UI text are in **Portuguese (PT-BR)**
- **Timezone**: `America/Sao_Paulo`
- **Language Code**: `pt-br`
- **Model Meta**: Models use `verbose_name` and `verbose_name_plural` for Portuguese labels
- **Static Files**: Served via WhiteNoise in production with compression
- **Admin**: Customized with Jazzmin theme (blue/cerulean color scheme)
- **Security**: Production mode enforces SSL, secure cookies, XSS protection, and clickjacking prevention
- **Image Uploads**: Stored in `media/` directory under app-specific subfolders (`produtos/`, `servicos/`, `profissionais/`)

---

## Database Configuration

The project uses `dj_database_url` for flexible database configuration. By default it expects a `DATABASE_URL` environment variable. The `docker-compose.yml` provides a PostgreSQL 15 setup on port 5435.

---

## Email Configuration

Email is configured for Gmail SMTP:
- Host: `smtp.gmail.com`
- Port: `587` (TLS)
- User: `miguelpaucar987@gmail.com`
- Password: via `EMAIL_HOST_PASSWORD` env var

---

## Notes

- The project uses **Django 6.0** (latest major version)
- No test files were found in the codebase; consider adding tests for models, views, and forms
- The `Autenticacao` app has no custom models (uses Django's built-in User model)
- Cart functionality is session-based (no database model for cart items)
- Orders are linked to authenticated users only
