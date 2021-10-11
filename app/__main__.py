"""Run flask app."""

# pylint: disable=wrong-import-position
from app import create_app

app = create_app()


if __name__ == "__main__":  # Only in dev
    app.run(host="0.0.0.0", port=8081, debug=True)

