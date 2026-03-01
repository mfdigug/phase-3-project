# Café Order Management System

A command-line ordering system for a café (selling caffeine only), built with Python and SQLAlchemy ORM.
This application allows users to create orders, add menu items and modify those items before reviewing, updating or deleting an order.

Here is a video demonstrating the functionality: ([CLI Cafe App Video](https://youtu.be/VUICVI0mVq4))

## Overview

This project simulates a basic Point of Sale (POS) system for a café. It demonstrates:

- Object-relational mapping using SQLAlchemy
- Relational database design
- Many-to-many relationships
- CCLI architecture
- Separation of concerns (models, helpers, CLI)

## Tech Stack

- python 3.8+
- SQLAlchemy ORM
- SQLite
- Alembic (for migrations)
- Pipenv
- Click

## Installation & Setup

1. Fork & clone the repo
2. cd into the project's directory
3. In the terminal, run:
   pipenv install; pipenv shell
   (this should install alembic, sqlalchemy, faker, click)
4. Run chmod +x cli.py to make the file executable
5. Run migrations to set up the db:
   alembic upgrade head
6. Run 'python seed.py' to seed fake data
7. Enter the application by calling:
   - cli.py
     OR
   - ./cli.py main-menu

Then follow the prompts

## CLI Flow:

1. Find custoer
2. New Order
3. Add Item
4. Finalise order
5. Exit

Top-level commands can also be called directly from the terminal, such as:

1. cli.py find-customer --email
2. cli.py new-order --customer-id
3. cli.py add-item --order-id
4. cli.py finalise-order --order-id

## Database Schema

### Models

#### Customer

- id
- first_name
- last_name
- Has many Orders

#### Order

- id
- customer_id
- Has many OrderItems

#### OrderItem

- id
- quantity
- order_id
- menu_item_id
- Belongs to an Order
- Belongs to a MenuItem
- Has many Mods (many-to-many)

#### MenuItem

- id
- item
- price
- Belongs to many OrderItems

#### Mod

- id
- mod_item
- mod_price
- Belongs to many OrderItems

#### order_item_mods (Association Table)

- order_item_id
- mod_id
