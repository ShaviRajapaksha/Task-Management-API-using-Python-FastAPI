# Task Management API

A production-ready RESTful API for task management built with **FastAPI** and **PostgreSQL**. Features user authentication, task categorization, and complete CRUD operations.

## Features

- User Authentication - JWT-based authentication with secure password hashing
- Task Management - Create, read, update, and delete tasks
- Task Categories - Organize tasks with custom categories
- Task Prioritization - Low, Medium, High priority levels
- Task Status Tracking - Pending, In Progress, Completed
- User Profiles - Each user has their own isolated data
- Automatic API Documentation - Interactive Swagger UI and ReDoc
- Database Migrations - SQLAlchemy ORM with PostgreSQL
- Input Validation - Pydantic models for data validation
- Error Handling - Comprehensive error responses
- Security - Password hashing, JWT tokens, SQL injection protection

## Tech Stack

- FastAPI - Web framework for building APIs
- PostgreSQL - Relational database
- SQLAlchemy - ORM for database operations
- Pydantic - Data validation and serialization
- python-jose - JWT token handling
- passlib - Password hashing
- psycopg2 - PostgreSQL adapter for Python
- Uvicorn - ASGI server

## Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip (comes with Python)
