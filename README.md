# Python ETL Pipeline with PostgreSQL

![Python](https://shields.io)
![PostgreSQL](https://shields.io)
![Pandas](https://shields.io)

A modular ETL (Extract, Transform, Load) pipeline built with Python that retrieves product and user data from the Fake Store API, transforms the data using Pandas, and loads the processed data into PostgreSQL. The project emphasizes clean code, modular design, logging, exception handling, and secure configuration management.

---

## Why I Built This Project

I built this project as part of my Data Engineering learning journey to gain hands-on experience with the complete ETL process.

Rather than simply extracting and storing data, I wanted to follow software engineering best practices by building a modular pipeline with proper logging, exception handling, and secure configuration using environment variables. This project helped me understand how production ETL pipelines are structured and how different components work together.

---

## Features

- Extracts product and user data from the Fake Store REST API
- Cleans and transforms raw JSON data using Pandas
- Loads transformed data into PostgreSQL
- Modular ETL architecture (`Extract` → `Transform` → `Load`)
- Structured logging for monitoring pipeline execution
- Exception handling with full tracebacks for reliable debugging
- Environment variable configuration using `.env`
- Easily extensible with additional data sources or transformations

---

## Project Architecture

```text
                Fake Store API
                       │
                HTTP Requests
                       │
             ┌─────────▼─────────┐
             │      Extract      │
             └─────────┬─────────┘
                       │
             ┌─────────▼─────────┐
             │    Transform      │
             └─────────┬─────────┘
                       │
             ┌─────────▼─────────┐
             │       Load        │
             └─────────┬─────────┘
                       │
                  PostgreSQL
                       │
                  Log File
```

---

## Project Structure

```text
First-Etl-Pipeline/
│
├── extract.py          # Extracts data from the API
├── transform.py        # Cleans and transforms data
├── load.py             # Loads data into PostgreSQL
├── logger.py           # Logging configuration
├── config.py           # Environment variable configuration
├── main.py             # Runs the ETL pipeline
├── .env                # Database credentials (ignored by Git)
├── .env.example        # Example environment variables
├── .gitignore
├── requirements.txt
├── etl.log
└── README.md
```

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pandas | Data cleaning and transformation |
| Requests | HTTP API requests |
| PostgreSQL | Relational database storage |
| SQLAlchemy | Database ORM and connection engine |
| psycopg2 | PostgreSQL database adapter |
| python-dotenv | Environment variable management |
| Logging | Pipeline execution monitoring |

---

## ETL Workflow

### 1. Extract
- Fetches product and user data from the Fake Store API.
- Converts raw JSON responses into Pandas DataFrames.

### 2. Transform
- **Product Data:** Renames columns, selects required fields, and casts prices to numeric formats.
- **User Data:** Flattens nested name and address dictionaries, renames columns, and filters required fields.

### 3. Load
- Connects to PostgreSQL using SQLAlchemy.
- Loads transformed DataFrames into the `products` and `users` tables (refreshing table data on each run).
- Safely closes database connections after execution.

---

## Logging & Exception Handling

Instead of `print()` statements, the pipeline uses Python's built-in `logging` module to write execution details to `etl.log`. It tracks pipeline start/completion, row counts at each stage, database connection states, and full exception tracebacks for API failures, connection errors, or transformation issues.

**Example Log Output:**
```text
INFO ETL Pipeline Started
INFO Starting product extraction.
INFO Successfully extracted 20 products.
INFO Starting user transformation.
INFO User transformation completed successfully.
INFO Successfully loaded 20 records into 'products'.
INFO ETL Pipeline Completed Successfully.
```

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/AbhiramT145/First-Etl-Pipeline.git
cd First-Etl-Pipeline
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up PostgreSQL & Environment Variables
Create a local PostgreSQL database named `fake_store_db`, then create a `.env` file in the root directory based on `.env.example`:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=fake_store_db
```

### 4. Run the Pipeline
```bash
python main.py
```

---

## Future Improvements

- Containerize the application using Docker and Docker Compose
- Schedule automated pipeline runs with Apache Airflow
- Implement rotating log files (`RotatingFileHandler`)
- Add automated unit tests with `pytest`
- Integrate schema and data validation checks (e.g., Pydantic or Great Expectations)
- Deploy the pipeline to a cloud environment

---

## Author

**Abhiram Bharadwaj**

---

## License

This project is created for learning and portfolio purposes.
