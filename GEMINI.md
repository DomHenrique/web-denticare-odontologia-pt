# Project Overview

This is a Django-based web application for a dental clinic named "DentiCare". The project is structured into several Django apps, each handling a specific functionality of the website.

**Main Technologies:**

*   **Backend:** Django
*   **Frontend:** HTML, CSS, JavaScript
*   **Database:** PostgreSQL
*   **Dependencies:** Pillow, psycopg2, django-bootstrap5, and others listed in `requirements.txt`.

**Architecture:**

The project follows a standard Django architecture, with the following apps:

*   `Inicio`: Handles the home page.
*   `Servicios`: Manages the services offered by the clinic.
*   `Productos`: Manages the products available for purchase.
*   `Carrito`: Implements the shopping cart functionality.
*   `Autenticacion`: Handles user authentication (login, registration).
*   `Pedido`: Manages orders.
*   `Contacto`: Provides a contact form.

# Building and Running

**1. Install Dependencies:**

```bash
pip install -r requirements.txt
```

**2. Apply Migrations:**

```bash
python manage.py migrate
```

**3. Run the Development Server:**

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

**4. Build for Production:**

The project includes a `build.sh` script that can be used for production builds.

```bash
./build.sh
```

# Development Conventions

*   **Coding Style:** The project follows the standard Python PEP 8 style guide.
*   **Database:** The project uses PostgreSQL for the database. The connection is configured in `DentiCareWeb/settings.py`.
*   **Static and Media Files:** Static files (CSS, JavaScript) are served using `whitenoise`. Media files (user-uploaded images) are stored in the `media` directory.
*   **Email:** The project is configured to send emails using a Gmail account. The settings are in `DentiCareWeb/settings.py`.
