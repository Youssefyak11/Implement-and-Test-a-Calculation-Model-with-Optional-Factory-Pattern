# Reflection – Module 11: Calculation Model, Validation, and CI/CD

(Write around 200–250 words.)

Possible points to cover:

- How defining the `Calculation` SQLAlchemy model helped you understand mapping Python classes to database tables.
- Why you chose to store the `result` and how that helps with later querying history.
- How Pydantic schemas (`CalculationCreate`, `CalculationRead`) helped with validation and JSON serialization/deserialization.
- How the factory pattern (Add/Subtract/Multiply/Divide strategies) makes your design more extensible if you add new operations.
- Challenges you faced setting up the database (SQLite vs PostgreSQL), tests, and GitHub Actions workflow.
- How CI/CD (automatic tests + Docker build and push) connects to DevOps principles and improves reliability.
- How this project demonstrates the course learning outcomes: automated testing, GitHub Actions, containerization with Docker, SQL integration, Pydantic validation, and security best practices via environment variables.
