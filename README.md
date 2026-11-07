# CS50 Final Project - Cryptocurrency Dashboard

A full-stack application that displays cryptocurrency data from CoinMarketCap API with a React frontend and FastAPI backend.

## Features

- Real-time cryptocurrency data display
- Interactive cryptocurrency list with detailed views
- Responsive UI with Ant Design components
- API integration with CoinMarketCap

## Project Structure

```
.
├── backend/                 # FastAPI backend
│   ├── src/                 # Source code
│   │   ├── main.py          # Main application entry point
│   │   ├── router.py        # API routes
│   │   ├── http_client.py   # HTTP client for CoinMarketCap API
│   │   ├── init.py          # Application initialization
│   │   └── config.py      # Configuration management
│   └── requirements.txt     # Python dependencies
├── frontend/                # React frontend
│   ├── src/                 # Source code
│   │   ├── App.jsx          # Main application component
│   │   ├── components/        # Reusable components
│   │   └── utils.js         # Utility functions
│   └── package.json         # Frontend dependencies
├── .env                     # Environment variables (API keys)
└── README.md                # This file
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install async-lru
   ```

3. Create a `.env` file with your CoinMarketCap API key:
   ```
   CMC_API_KEY=your_api_key_here
   ```

4. Run the backend server:
   ```bash
   python -m uvicorn src.main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file with your backend API URL:
   ```
   REACT_APP_API_BASE_URL=http://localhost:8000
   ```

4. Run the development server:
   ```bash
   npm run dev
   ```

## Development Guidelines

1. All code should follow consistent naming conventions (English only)
2. Use proper error handling and logging
3. Add documentation for all functions and components
4. Write unit tests for all components
5. Follow React best practices for state management

## Security Considerations

1. Never commit API keys to version control
2. Use environment variables for sensitive data
3. Implement proper CORS settings
4. Add input validation and sanitization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is licensed under the MIT License.