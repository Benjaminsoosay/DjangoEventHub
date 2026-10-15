# Django Event Hub

## Description
DjangoEventHub is a web application built using the Django framework. It is designed to allow users to browse, view, and book events. The application utilizes a SQLite database and includes a fully functional administrative backend.

## Purpose
The purpose of this software is to fulfill the requirements for the Web Apps module. It demonstrates the ability to create a full-stack web application using Django, including database modeling, form handling, template rendering, and user interaction.

## Demonstration
A video demonstration of the software can be viewed at the following link: 
[Loom Video Demonstration](https://www.loom.com/share/46e24049329e43cd88e9e9fb9e6347ca)

## Repository
The source code for this project is available on GitHub:
[DjangoEventHub GitHub Repository](https://github.com/Benjaminsoosay/DjangoEventHub)

## Web Pages
The application includes the following web pages:
*   **Home / Event List:** The landing page that displays a list of all available events to the user.
*   **Event Details:** A page displaying specific information about a selected event.
*   **Booking Page:** A form page where users can input their information to book a spot for an event.
*   **Admin Panel:** The Django built-in admin interface used to manage events, bookings, and user data.

## Technologies Used
*   **Framework:** Django (Python)
*   **Database:** SQLite (`db.sqlite3`)
*   **Frontend:** HTML, CSS (via Django Templates)
*   **Other:** Django Forms, Django Models

## Installation and Setup
To run this project locally, follow these steps:
1. Clone the repository to your local machine:
   `git clone https://github.com/Benjaminsoosay/DjangoEventHub.git`
2. Install the required dependencies:
   `pip install -r requirements.txt`
3. Apply database migrations:
   `python manage.py migrate`
4. Start the development server:
   `python manage.py runserver`
5. Open your web browser and navigate to `http://127.0.0.1:8000/`

## Author
Benjamin
