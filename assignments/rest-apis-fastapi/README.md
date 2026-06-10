# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a modern REST API using FastAPI, a high-performance web framework for Python. You'll create endpoints that handle HTTP requests and return structured JSON responses, implementing best practices for API design.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Application

#### Description
Build a basic FastAPI application with a simple endpoint that accepts requests and returns JSON responses. Set up the project structure and understand how FastAPI handles routing and request/response handling.

#### Requirements
Completed application should:

- Import and instantiate a FastAPI application
- Define at least two routes (GET endpoints) that return JSON data
- Use proper Python type hints for request and response data
- Be runnable with `uvicorn` server
- Return appropriate HTTP status codes

### 🛠️ Add Dynamic Routes and Path Parameters

#### Description
Extend your API by adding routes that accept path parameters and query parameters. Create endpoints that simulate retrieving data based on user input.

#### Requirements
Completed application should:

- Include routes with path parameters (e.g., `/items/{item_id}`)
- Include routes with query parameters (e.g., `/items?skip=0&limit=10`)
- Validate input parameters appropriately
- Return different responses based on the provided parameters
- Include at least one POST endpoint that accepts JSON request body data

### 🛠️ Implement a Simple Data Store (Stretch Goal)

#### Description
Build a more realistic API that manages a simple data store in memory. This will help you understand how APIs interact with data.

#### Requirements
Completed application should:

- Store data items in memory (e.g., a list or dictionary)
- Implement GET, POST, and DELETE operations
- Maintain data consistency across API calls
- Return appropriate error responses when data is not found (404 status code)
- Include proper documentation in docstrings for each endpoint
