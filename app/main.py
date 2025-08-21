import uvicorn
import os

if __name__ == "__main__":
    db_url = os.environ.get("DB_URL")
    if db_url:
        print(f"Connecting to MongoDB with URL: {db_url}")
    
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)