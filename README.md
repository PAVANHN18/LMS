# Leave Management System - MVP
FastAPI + PostgreSQL + Render Deployment

## Setup Steps
1. Install dependencies:
   pip install -r requirements.txt
2. Set environment variable:
   DATABASE_URL=<your_postgres_url>
3. Run locally:
   uvicorn src.main:app --reload
4. Deploy to Render with DATABASE_URL in environment.

## API Endpoints
- POST /employees/
- GET /employees/{emp_id}/leave-balance

## Potential Improvements
- Authentication
- Email notifications
- Detailed leave history
