from app.database.database import Database
from app.controller.controller import WWController


database = Database()
controller = WWController(database)

