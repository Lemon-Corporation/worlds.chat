from app.db.database import Base, engine
from app.models.user import User

# Создание всех таблиц
Base.metadata.create_all(bind=engine)

print("Таблицы успешно созданы!")