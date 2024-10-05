# Text-to-RDBMS

Text-to-RDBMS is an AI-powered system that enables users to interact with their relational databases through natural language. Simply describe your data needs in plain text, and the system will automatically generate and execute SQL queries on your database, returning results in an intuitive format.

## Features

- **Natural Language Querying:** Generate SQL queries based on natural language input using OpenAI's API.
- **Database Schema Reader:** Automatically extract schema information (tables, columns, relationships) from any connected database.
- **Secure Query Execution:** Execute generated SQL queries against the database securely with proper validation.
- **Result Presentation:** Display query results in an easy-to-understand format, including tables and visualizations.
- **Simple User Interface:** A lightweight and responsive UI built using HTML, JavaScript, and CSS.

## Tech Stack

- **Frontend:** HTML, JavaScript, and CSS
- **Backend API:** Node.js (Express) or Python (Flask/FastAPI)
- **Database Connectivity:** Native database clients or ORMs (e.g., SQLAlchemy for Python)
- **AI Model Integration:** OpenAI API for text-to-SQL conversion
- **Data Visualization:** HTML tables and optional JavaScript chart libraries for visualizations

## Getting Started

### Prerequisites

- **Node.js**: v14+ or **Python**: v3.7+
- **Database**: MySQL, PostgreSQL, SQLite, or any other supported RDBMS
- **API Key**: OpenAI API key for generating SQL queries

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/text-to-rdbms.git
   cd text-to-rdbms

## Install Backend Dependencies

For Node.js Backend:
```bash
npm install
```

For Python Backend:
```bash
pip install -r requirements.txt
```

Environment Variables

OpenAI API Key: Set your OpenAI API key in the .env file in the root directory.
Database Configuration: Set database connection details in .env.
env
Copy code
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=your_database_connection_string
Running the Project
Start Backend Server

For Node.js:
bash
Copy code
npm run start
For Python:
bash
Copy code
python app.py
Access the UI

Open the index.html file located in the ui directory in your preferred web browser.
Usage
Connect Database:
Provide database credentials to connect the system to your database.
View Schema:
The system will automatically extract and display the schema of your database.
Ask a Query:
Enter a natural language query (e.g., "Show all customers from California").
Get Results:
The system will generate and execute an SQL query based on your input and display the results.
Development
Project Structure
markdown
Copy code

## Folder Structure

text-to-rdbms/
│
├── db-reader/                    # Reads the database schema 
│   ├── index.js / schema_reader.py  # Main code for extracting schema details
│   └── ...                       # Any additional modules for DB connection
│
├── nlp-query-generator/          # NLP code to generate SQL from user input
│   ├── index.js / query_generator.py
│   └── openai_integration.js / openai_integration.py
│
├── response-formatter/           # Code to format query results for display
│   ├── index.js / response_formatter.py
│   └── utils.js / utils.py       # Utility functions for formatting results
│
├── ui/                           # Frontend code
│   ├── index.html               # Main HTML file
│   ├── styles.css               # CSS for styling
│   └── app.js                   # JavaScript for UI interactions
│
├── docs/                         # Documentation and assets
├── .env                          # Environment variables
└── README.md                     # Project documentation

Adding a New Feature
Create a new branch for your feature:



### Contributing
Contributions are welcome! Please open an issue or submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contact
For any questions or suggestions, please open an issue or contact the project owner at s@shamsher.info.
