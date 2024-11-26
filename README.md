# HTTP Response Code Manager 🐾

A full-stack web application that enables users to explore, filter, save, and manage HTTP response codes alongside their corresponding dog images fetched dynamically from [http.dog](https://http.dog). This project simplifies understanding HTTP status codes in a fun and engaging way by visualizing them with cute dog images. 🐶

## Features

### 🌐 **Core Functionality**
- **Explore HTTP Codes**: View and understand various HTTP response codes with visual representation via dog images.
- **Dynamic Search**: Filter HTTP codes using regex-like patterns (e.g., `2xx`, `4xx`) for flexible searching.
- **CRUD Operations**: Create, edit, view, and delete personalized lists of HTTP response codes.

### 🔐 **User Management**
- Secure user registration and login using Django's built-in authentication system.
- User-specific saved lists for managing custom collections.

### 🚀 **Dynamic Integration**
- Real-time fetching of dog images corresponding to HTTP response codes via API integration.
- Search filters that dynamically update the displayed results.

### 🎨 **Tech Stack**
- **Backend**: Python, Django, SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite for data persistence
- **APIs**: External integration with [http.dog](https://http.dog)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/http-response-code-manager.git
   cd http-response-code-manager
