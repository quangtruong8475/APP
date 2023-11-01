from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app import db, app
from sqlalchemy.orm import relationship


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('product', backref='category',lazy=True )


class Product(db.Model):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    img = Column(String(100), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='mobile')
        # c2 = Category(name='table')
        db.create_all()
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
