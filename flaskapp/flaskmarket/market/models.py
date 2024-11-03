from market import db,app
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)


def add_item(name, price, barcode, description):
    with app.app_context():
        if not Item.query.filter_by(description=description).first():
            item = Item(name=name, price=price, barcode=barcode, description=description)
            db.session.add(item)
            db.session.commit() 
           
