# Demo E-Commerce Application

A simple e-commerce application for demonstrating the Context-Aware Code Generation Agent.

## Features

- User management
- Product catalog
- Order processing
- Email notifications
- Payment processing

## Structure

```
demo_repository/
├── utils/
│   ├── validators.py    # Input validation utilities
│   ├── email.py         # Email handling
│   └── formatters.py    # Data formatting
├── services/
│   ├── user_service.py  # User management
│   ├── product_service.py # Product operations
│   └── order_service.py # Order processing
└── models/
    └── data_models.py   # Data models
```

## Usage

This repository is designed to showcase code reuse patterns and demonstrate
how the Context-Aware Code Generation Agent can generate new code while
maximizing reuse of existing utilities and functions.