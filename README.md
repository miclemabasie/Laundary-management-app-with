# Laundry Management System - API

# Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
4. [Running the Application in a Container](#running-the-application-in-a-container)
5. [API Endpoints](#api-endpoints)
6. [Usage](#usage)
8. [License](#license)
9. [Contact](#contact)


## Overview

The Laundry Management System API serves as the backend for a comprehensive solution designed to streamline laundry services. It facilitates communication between shop owners, customers, and the database. This Django-based API offers secure user authentication, order processing, subscription plans, and a review system.

## Features

- **User Authentication:** Secure authentication system for shop owners and customers.
- **Subscription Plans:** Flexible subscription plans with varying levels of access and features.
- **Order Processing:** Efficient order processing with real-time updates for customers and shop owners.
- **Review System:** Integrated review system allowing customers to provide feedback on services.

## Setup

### Prerequisites

- Python 3.x
- Virtual Environment (optional but recommended)

### Installation

1. Clone the repository by running the following command:
   ```git clone https://github.com/miclemabasie/Laundary-management-app-with.git```

2. Navigate to the ```src``` directory with the following command:
    ```cd src```

3. Install project dependencies, run the following command: 
    ```pip install -r requirements.txt```

4. Configure environment variables, copy the sample environment variables from the ```.env.example``` file inside the ```src``` directory and fill in as per you needs.
``` DEBUG=
SECRET_KEY=
POSTGRES_ENGINE=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
SIGNING_KEY=
```
5. Run the development server
    ```python manage.py runserver```

## Running the application in a container

1. After configuring your environment variables, run the following command to make sure there are being reflected in the ```docker compose``` configuration.
    ```docker compose config```
You should see the full configuration if set up if everyting is of
Incase of difficulty contact me at info@techwithmiclem.com to help you resolve the issue.


### API Endpoints

| HTTP Method | Endpoint            | Description                           |
|-------------|---------------------|---------------------------------------|
| POST         | /api/v1/auth/users/ | Register a new user (shop owner or customer). |
| POST        | /api/v1/auth/jwt/create/   | Log in and obtain an authentication token.    |
| POST        | /api/v1/auth/users/activation   | Activate a new user account.    |
| GET         | /api/v1/plans/         | List all available subscription plans.      |
| POST        | /api/v1/subscribe/     | Subscribe to a specific plan.              |
| GET         | /api/v1/orders/        | List all orders.                           |
| POST        | /api/v1/orders/create/ | Create a new order.                        |
| GET         | /api/v1/reviews/       | List all reviews.                          |
| POST        | /api/v1/reviews/create/| Create a new review.                       |


## Usage
Shop Owners: Utilize the provided API endpoints for managing orders, subscriptions, and other shop-related details.
Customers: Interact with the API to place orders, track order status, and submit reviews.
Contributing
If you'd like to contribute to this project, please follow the Contribution Guidelines.

## License
This project is licensed under the MIT License.

## Contact
For inquiries or support, please contact me at [info@techwithmicle.com](info@techwithmicle.com).

This README is more focused on the API part of the project, providing clear information on features, setup, available endpoints, and how users (both shop owners and customers) can interact with the API.



