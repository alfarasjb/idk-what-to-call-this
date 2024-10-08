from src.server.api import app
import uvicorn
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    uvicorn.run(app=app, host='0.0.0.0', port=8080)
