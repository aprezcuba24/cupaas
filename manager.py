from app import app
from app import github_webhook

if __name__ == "__main__":
    app.run(host="0.0.0.0")
