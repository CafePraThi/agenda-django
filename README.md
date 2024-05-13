# Django Agenda Project

## Introduction

This is a Django-based agenda project aimed at managing contacts. The project includes features such as user authentication, profile management, contact creation, grouping contacts, and activating/deactivating contacts.

## Installation

1. Clone the repository to your local machine:

```
git clone <repository_url>
```

2. Navigate to the project directory:

```
cd django-agenda-project
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Apply migrations to set up the database:

```
python manage.py migrate
```

5. Create a superuser to access the admin interface:

```
python manage.py createsuperuser
```

6. Start the development server:

```
python manage.py runserver
```

7. Access the application at `http://localhost:8000` in your web browser.

## Usage

### User Authentication

Users can register and log in to the application to access their personal contacts. They can also update their profiles and log out when necessary.

### Contact Management

- **Creating Contacts**: Users can add new contacts by providing relevant information such as name, phone number, email, etc.
  
- **Grouping Contacts**: Contacts can be organized into groups for better management. Users can create, edit, or delete groups as needed.

- **Activating/Deactivating Contacts**: Users can toggle the status of their contacts to activate or deactivate them. Deactivated contacts are not displayed in the active contact list.

### Admin Interface

Administrators can access the admin interface to manage users, groups, and contacts efficiently.

