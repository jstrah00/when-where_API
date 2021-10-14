"""Run flask app."""

# pylint: disable=wrong-import-position
from app import create_app

flask_app = create_app()

def main() -> None:
    flask_app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == "__main__":  # Only in dev
    main()

