1. Install Flask (CMD)
pip install Flask
pip install flask-bcrypt
pip install Flask-SQLAlchemy
pip install Flask-WTF
pip install Flask-login
pip install email_validator

from H2GO import db
db.create_all()
db.drop_all()

User.query.all()
from H2GO.models import User, Order, Shipment, Product

from H2GO import db
db.create_all()
from H2GO.models import Time_Pickup
time1 = Time_Pickup(time="0900")
db.session.add(time1)
db.session.commit()
Time_Pickup.query.all()

shit=Time_Pickup.query.filter_by(time="0900").first()
print(Time_Pickup.query.filter_by(time="0900").first().time_count)

