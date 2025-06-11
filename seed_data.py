from app import create_app, db
from app.models import User, Book
from flask_bcrypt import Bcrypt

app = create_app()
bcrypt = Bcrypt()

with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(
        username='admin',
        password=bcrypt.generate_password_hash('admin123').decode('utf-8'),
        is_admin=True
    )
    db.session.add(admin)

    books = [
        Book(title='1984', author='George Orwell', language='English', publication_year=1949),
        Book(title='The Little Prince', author='Antoine de Saint-Exupéry', language='French', publication_year=1943),
        Book(title='Harry Potter', author='J.K. Rowling', language='English', publication_year=1997)
    ]
    db.session.add_all(books)
    db.session.commit()

    print("✅ Data seeded into MySQL.")
