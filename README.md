https://drive.google.com/file/d/1__5MOaTqBfxRi5W2pYVwrPst60vIM6a7/view?usp=sharing

🚀 How to Run the Marketplace Project
This guide will help you set up and run the Django Marketplace Project using Docker and PostgreSQL.

✅ 1. Prerequisites
Make sure you have the following installed:
Docker & Docker Compose (Download)
Postman (for API testing)
Git
✅ 2. Clone the Repository
git clone https://github.com/your-repo/marketplace.git
cd marketplace
✅ 3. Environment Configuration
Create a .env file in the project root and set your environment variables:
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=*
DATABASE_URL=postgres://marketplace_user:password@db:5432/marketplace_db
REDIS_URL=redis://redis:6379/0
📌 Make sure DATABASE_URL matches your PostgreSQL container settings.

✅ 4. Run the Project with Docker
docker-compose up --build -d
✔ This will start Django, PostgreSQL, Redis, and Celery inside Docker containers.

✅ 5. Apply Migrations & Create Superuser
docker exec -it marketplace_web python manage.py makemigrations
docker exec -it marketplace_web python manage.py migrate
docker exec -it marketplace_web python manage.py createsuperuser
📌 Follow the prompts to create an admin user.

✅ 6. Collect Static Files (For Production)
docker exec -it marketplace_web python manage.py collectstatic --noinput
docker-compose restart nginx
📌 Now, static files will be served correctly via Nginx.

✅ 7. Access the Application
🌍 Open in Browser:

API Docs (Swagger): http://127.0.0.1:8000/swagger/
Admin Panel: http://127.0.0.1:8000/admin/
Frontend Homepage: http://127.0.0.1:8000/
📌 Use the superuser credentials to log in to the admin panel.

✅ 8. Testing APIs with Postman
Use Bearer Authentication with JWT tokens:

Login to get the token:
POST http://127.0.0.1:8000/api/users/login/
Content-Type: application/json  
Body:  
{  
    "username": "admin",  
    "password": "yourpassword"  
}
Use the access token in headers:
Authorization: Bearer your_access_token
✅ 9. Stopping and Restarting the Project
🔹 Stop the project:

docker-compose down
🔹 Restart the project without rebuilding:

docker-compose up -d
🔹 Rebuild everything if needed:

docker-compose up --build -d
🎯 Project Structure
marketplace/
│── marketplace/          # Django settings & project config
│── products/             # Product app (models, views, API)
│── users/                # User authentication & profiles
│── trading/              # Trading & marketplace logic
│── sales/                # Payment & order management
│── cart/                 # Shopping cart system
│── analytics/            # Reports & statistics
│── notifications/        # User notifications
│── templates/            # Frontend (HTML templates)
│── static/               # CSS, JS, images
│── media/                # Uploaded product/user images
│── docker-compose.yml    # Docker services config
│── Dockerfile            # Django container config
│── requirements.txt      # Dependencies
│── .env                  # Environment variables
🎉 Congratulations! Your Marketplace Project is now running! 🚀
If you have any issues, check the logs:

docker-compose logs -f web
🔥 Happy coding! 💪
