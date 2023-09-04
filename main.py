from model import database
from view import main_window

if __name__ == "__main__":
    database.connect_db()
    main_window.initialize_view()
