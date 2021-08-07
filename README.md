# Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [End-points](#end-points)
* [Setup](#setup)
---

### General info
Sequence Integers API	

### Technologies
Project is created with:
* [Python](https://svelte.dev/)
* [Django Ninja REST](https://django-ninja.rest-framework.com/)
	
### End-points
1. Auth
   - POST: `/api/v1/auth/register` 
   - POST: `/api/v1/auth/login`
   - GET: `/api/v1/auth/me`

2. Count
   - GET: `/api/v1/count/current`
   - GET: `/api/v1/count/next`
   - PUT: `/api/v1/count/current`

> Swagger API documentations `/api/v1/docs`

> Admin dashboard `/admin`
### Setup
To run this project, follow up these steps:

1. Create a virtual environment
   - `python3 -m venv venv`.

2. Activate the environment
   - For MAC/Linux:`source venv/bin/activate`.
   - For Windows: `venv\Scripts\activate.bat`.

3. Install packages and dependencies
   - `pip3 install -r requirements.txt`

4. Create tables and make the migrations
   - `python3 manage.py makemigrations` and then `python3 manage.py migrate`

5. Run the server
   - `python3 manage.py runserver`

