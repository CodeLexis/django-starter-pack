# Django Starter Pack

A comprehensive template to kickstart your Django projects with best practices and essential configurations.

## Features

- **Django 4.2.13**: Leverage the latest features and improvements of Django.
- **Docker Support**: Facilitates containerized development and deployment.

## Getting Started

### Prerequisites

- **Python 3.9** or higher
- **Docker** (optional, for containerized development)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/codedby-tomisin-dev/django-starter-pack.git
   cd django-starter-pack
   ```

2. **Set Up Environment Variables**:

   ```bash
   cp .env.local.example .env.local
   cp .env.shared.example .env.shared
   cp .env.test.example .env.test
   # Edit .env to configure your environment variables
   ```

3. **Install Dependencies**:

   ```bash
   python -m venv .venv
   source ./.venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000`. View the test endpoint at `http://127.0.0.1:8000/sample/hello`

## Docker Deployment

1. **Build the Docker Image**:

   ```bash
   docker build -t django-starter-pack .
   ```

2. **Run the Docker Container**:

   ```bash
   docker run -d -p 8000:80 --env-file .env --name django_starter_container django-starter-pack
   ```

   The application will be accessible at `http://localhost:8000`.

## Usage
- **Sample Service**: A sample service is included in `services/sample`. Clone the directory and build it out to your taste.
- **Admin Interface**: Navigate to `/admin` to access the Django admin panel.
- **User Authentication**: User registration and login are available at `/identity`.
- **Static Files**: Static files are served from the `/static/` directory.
- **Monitoring**: Sentry is wired up for this project. Set a `SENTRY_DSN` environment variable to complete the Sentry setup.
- **Background Tasks**: [Celery + Redis configuration](https://testdriven.io/courses/django-celery/getting-started/) is wired up to handle background tasks.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Inspired by various Django starter templates and best practices.
