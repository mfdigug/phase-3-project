# Café Order Management System

A command-line ordering system for a café (selling caffeine only), built with Python and SQLAlchemy ORM.
This application allows users to create orders, add menu items and modify those items before reviewing, updating or deleting an order.

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
4. Run migrations to set up the db:
   alembic upgrade head
5. Enter the application:
   python lib/cli.py

Then follow the prompts

## CLI Flow:

1. Find custoer
2. New Order
3. Add Item
4. Add mod to item
5. Finalise order
6. Exit

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
