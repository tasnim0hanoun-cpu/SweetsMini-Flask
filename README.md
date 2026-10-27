
# Sweets Mini – Flask Recipe Application

## Project Description

Sweets Mini is a simple recipe management web application built with Python and Flask.

The project was developed as an individual in-depth study for the course Webbutveckling med ramverk (C1UT1B).

It is based on the same recipe-sharing concept as Sweets from Laboratory Assignment 2, which was developed using ASP.NET Core MVC.

## Framework

- Python
- Flask 3.1.3
- HTML and CSS
- Jinja2 templates

## Features

The application implements CRUD operations for recipes:

- Create – Add new recipes.
- Read – Display all recipes.
- Update – Edit existing recipes.
- Delete – Remove recipes.

## How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python app.py
   ```

5. Open http://127.0.0.1:5000 in your browser.

## Implementation

Flask routes handle HTTP requests and recipe operations.

Recipes are stored in a Python list in memory. No external database is required for this prototype.

Data is reset when the application restarts.

## Comparison with Lab 2

Sweets Mini uses Flask, while the original Sweets application uses ASP.NET Core MVC and Entity Framework Core.

The purpose is to compare framework architecture, routing, development experience and application structure.

## Limitations

This is a small educational prototype. It does not include authentication, persistent database storage or cloud deployment.
