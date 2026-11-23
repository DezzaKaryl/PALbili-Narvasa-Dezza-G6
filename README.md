# PALbili-Narvasa-Dezza-G6

# PALbili: Your Store to Door Pal

Same-day shopping and delivery application. Built with Django and PostgreSQL (Supabase).

**Course:** IT317 Project Management, G6
**Developer:** Dezza Karyl P. Narvasa

## Features (Account Module)
- Registration with validation and hashed passwords
- Login / Logout
- Role-based dashboards (Customer, Rider, Administrator)
- User profile view and edit (with profile photo)

## Setup
1. Clone the repository
2. Create and activate a virtual environment:
   `python -m venv venv` then `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill in your database credentials
5. Run migrations: `python manage.py migrate`
6. Create an admin: `python manage.py createsuperuser`
7. Start the server: `python manage.py runserver`