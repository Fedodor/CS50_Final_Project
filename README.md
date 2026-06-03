# CS50 Final Project

![FastAPI](https://img.shields.io/badge/FastAPI-Backend-informational?logo=fastapi)
![React](https://img.shields.io/badge/React-Frontend-informational?logo=react)
![Vite](https://img.shields.io/badge/Vite-Build%20Tool-informational?logo=vite)
![CS50](https://img.shields.io/badge/CS50-Final%20Project-informational)

This is my final project for CS50x: a small full-stack web application built with a FastAPI backend and a React frontend.

The goal was not to build a huge product, but to connect the main parts of a modern web app: an API, data validation, async backend logic, a frontend interface, and communication between both sides.

## Demo

Video demo: https://youtu.be/14pbbAfhqMw

<!-- Optional: add screenshots later
## Screenshots

![Dashboard screenshot](docs/images/dashboard.png)
![Mobile view](docs/images/mobile.png)
-->

## Tech stack

**Backend**

- Python
- FastAPI
- Pydantic / pydantic-settings
- aiohttp

**Frontend**

- React
- Vite
- Ant Design
- Tailwind CSS

## What the app includes

- A FastAPI backend with structured request/response validation
- Async HTTP logic with `aiohttp`
- A React frontend built with reusable components
- A dashboard-style interface
- Basic CRUD-style data management
- Responsive UI work with Tailwind CSS and Ant Design

## What I practiced

This project helped me move from separate programming exercises to a complete web application. The main things I practiced were:

- designing API endpoints
- validating data with Pydantic
- connecting frontend and backend code
- working with async Python
- organizing a React project
- making a UI usable on different screen sizes
- documenting a project clearly enough for another person to run it

## Project structure

```text
CS50_Final_Project/
├── backend/
│   ├── src/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.js
└── README.md
```

## Run locally

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install uvicorn
uvicorn src.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

API docs:

```text
http://127.0.0.1:8000/docs
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend will run at:

```text
http://127.0.0.1:5173
```

## Future improvements

- Add automated backend tests
- Add frontend tests
- Improve error handling in the UI
- Add user roles and permissions
- Add WebSocket notifications or live updates
- Prepare a Docker Compose setup for easier local launch
