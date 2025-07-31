# Contact Form API Documentation

This document describes the REST API endpoints for the contact form functionality.

## Base URL
```
https://fullstacktanay-production.up.railway.app
```

## Endpoints

### 1. Create Contact Message
**POST** `/api/contacts`

Creates a new contact message in the database.

#### Request Body
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Hello, I'm interested in your iOS development services."
}
```

#### Response (Success - 201)
```json
{
  "message": "Contact message sent successfully",
  "status": "success"
}
```

#### Response (Error - 400)
```json
{
  "error": "Name is required"
}
```

### 2. Get All Contacts
**GET** `/api/contacts`

Retrieves all contact messages from the database.

#### Query Parameters
- `limit` (optional): Number of contacts to return (default: 50)

#### Example Request
```
GET /api/contacts?limit=10
```

#### Response (Success - 200)
```json
{
  "contacts": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "message": "Hello, I'm interested in your iOS development services.",
      "created_at": "2024-01-15T10:30:00Z"
    }
  ],
  "count": 1
}
```

### 3. Get Contact by ID
**GET** `/api/contacts/{id}`

Retrieves a specific contact message by ID.

#### Example Request
```
GET /api/contacts/1
```

#### Response (Success - 200)
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Hello, I'm interested in your iOS development services.",
  "created_at": "2024-01-15T10:30:00Z"
}
```

#### Response (Error - 404)
```json
{
  "error": "Contact not found"
}
```

### 4. Delete Contact
**DELETE** `/api/contacts/{id}`

Deletes a specific contact message by ID.

#### Example Request
```
DELETE /api/contacts/1
```

#### Response (Success - 200)
```json
{
  "message": "Contact deleted successfully"
}
```

#### Response (Error - 404)
```json
{
  "error": "Contact not found"
}
```

## Database Schema

### Contacts Table
```sql
CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## Environment Variables

The following environment variables are required for MySQL connection:

- `MYSQL_HOST`: MySQL server hostname
- `MYSQL_PORT`: MySQL server port (default: 3306)
- `MYSQL_USER`: MySQL username
- `MYSQL_PASSWORD`: MySQL password
- `MYSQL_DATABASE`: MySQL database name

## Error Handling

All endpoints return appropriate HTTP status codes:

- `200`: Success
- `201`: Created
- `400`: Bad Request (validation errors)
- `404`: Not Found
- `500`: Internal Server Error

Error responses include a JSON object with an `error` field containing the error message.

## Testing the API

### Using curl

1. **Create a contact:**
```bash
curl -X POST https://fullstacktanay-production.up.railway.app/api/contacts \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "message": "This is a test message"
  }'
```

2. **Get all contacts:**
```bash
curl https://fullstacktanay-production.up.railway.app/api/contacts
```

3. **Get specific contact:**
```bash
curl https://fullstacktanay-production.up.railway.app/api/contacts/1
```

4. **Delete contact:**
```bash
curl -X DELETE https://fullstacktanay-production.up.railway.app/api/contacts/1
```

### Using JavaScript

```javascript
// Create contact
const response = await fetch('/api/contacts', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        name: 'John Doe',
        email: 'john@example.com',
        message: 'Hello!'
    })
});

const result = await response.json();
console.log(result);
``` 