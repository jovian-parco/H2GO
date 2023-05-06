from H2GO import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    customer_id = db.Column(db.Integer, primary_key=True, )
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(69), unique=False, nullable=False)
    last_name = db.Column(db.String(69), unique=False, nullable=False)
    phone_number = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(100), unique=False, nullable=False)
    image_file = db.Column(db.String(20), unique=False, nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    orders = db.relationship("Order", backref="user", lazy=True)

    def __repr__(self):
        return f"User('{self.customer_id}','{self.username}','{self.first_name}','{self.last_name}','{self.address}','{self.password}')"

    def get_id(self):
        return (self.customer_id)


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.customer_id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"), nullable=False)
    shipment_id = db.Column(db.Integer, db.ForeignKey("shipment.shipment_id"), nullable=False)

    def __repr__(self):
        return f"Order('{self.order_id}','{self.customer_id}')"


class Shipment(db.Model):
    shipment_id = db.Column(db.Integer, primary_key=True)
    is_delivery = db.Column(db.Boolean, nullable=False)
    time_pickup = db.Column(db.String(69), nullable=False)
    time_delivery = db.Column(db.String(69), nullable=False)
    shipment = db.relationship("Order", backref="shipment", lazy=True)

    # shipment = db.relationship("Order", backref="shipment", lazy=True, uselist=False)

    def __repr__(self):
        return f"Shipement('{self.shipment_id}','{self.time_pickup}','{self.time_delivery}')"


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_6l_round = db.Column(db.Integer, unique=False, nullable=False, default=0)
    product_5g_round = db.Column(db.Integer, unique=False, nullable=False, default=0)
    product_5g_slim = db.Column(db.Integer, unique=False, nullable=False, default=0)
    products = db.relationship("Order", backref="product", lazy=True)

    def __repr__(self):
        return f"Product('{self.product_id}','{self.product_6l_round}','{self.product_5g_round}','{self.product_5g_slim}"

class Time_Pickup(db.Model):
    column_not_exist_in_db = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String, unique=False, nullable=False)
    time_count = db.Column(db.Integer, nullable=False, default=0)
    # am0900 = db.Column(db.Integer, unique=False, nullable=False, default=0)  # max number 5
    # am1000 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # am1100 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1200 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1300 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1400 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1500 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1600 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    def __repr__(self):
        return f"Time_Pickup('{self.time}','{self.time_count}')"

class TimeDelivery(db.Model):
    column_not_exist_in_db = db.Column(db.Integer, primary_key=True)
    # am1000 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # am1010 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # am1020 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # am1030 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # am1040 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # am1050 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # am1100 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # am1110 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # am1120 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # am1130 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # am1140 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # am1150 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1200 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1210 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1220 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1230 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1240 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1250 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1300 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1310 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1320 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1330 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1340 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1350 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1400 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1410 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1420 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1430 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1440 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1450 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1500 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1510 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1520 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1530 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1540 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1550 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1600 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1610 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1620 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1630 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1640 = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # pm1650 = db.Column(db.Integer, unique=False, nullable=False, default=0)
