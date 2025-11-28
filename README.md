RESTAPI-JOBSITE

Table of Contents

Project Overview
Features
Tech stack
API Overview
Authentication
Project Overview

RESTAPI-JOBSITE is a backend application that exposes RESTful endpoints for managing job postings, applications, and user accounts for a job board/site.

Features

User registration and authentication
CRUD operations for job postings
Apply to jobs and manage applications
Role-based access control (admin, employer, applicant)
Input validation and error handling
Tech stack

DRF
SQLite
Token for authentication
API Overview

This section should document the main endpoints. Example endpoints (update with actual routes):

POST /api/auth/register - Register a new user
POST /api/auth/login - Authenticate and receive a Token
POST /api/jobs - Create a new job (auth required, e.g. employer)
GET /api/jobs/:id - Get job details
PATCH/PUT /api/jobs/:id - Update a job (auth/permission required)
DELETE /api/jobs/:id - Delete a job (auth/permission required)
POST /api/jobs/:id/apply - Apply to a job (auth required)
Authentication

The API uses token-based authentication. Protect endpoints by providing the Authorization header:

Authorization: token
