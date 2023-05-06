from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, IntegerField, PasswordField, SubmitField, SelectField, DateTimeLocalField, BooleanField
from wtforms.validators import DataRequired, Length, number_range, EqualTo, Regexp, ValidationError
from H2GO.models import User, Product, Shipment, Order, Time_Pickup, TimeDelivery
from datetime import datetime



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=69)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=69)])
    phone_number = StringField('Phone', validators=[DataRequired(), Length(min=11, max=11), Regexp(regex='[0-9]')],render_kw={"placeholder": "09XXXXXXXXX"})
    address = StringField('Address', validators=[DataRequired(), Length(min=10, max=100)],render_kw={"placeholder": "Rm./Fl., Street.no, Baranggay, City/Town"})
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2, max=69)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already exists!")

    def validate_phone_number(self, phone_number):
        user = User.query.filter_by(phone_number=phone_number.data).first()
        if user:
            raise ValidationError("Phone number already exists!")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=6, max=20)])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=69) ])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=69)])
    phone_number = StringField('Phone', validators=[DataRequired(), Length(min=11, max=11), Regexp(regex='[0-9]')],render_kw={"placeholder": "09XXXXXXXXX"})
    address = StringField('Address', validators=[DataRequired(), Length(min=10, max=100)],render_kw={"placeholder": "Rm./Fl., Street.no, Baranggay, City/Town"})
    image_file = FileField("Update Profile Picture", validators=[FileAllowed(["jpg","png"])])
    submit = SubmitField("Update")


    def validate_phone_number(self, phone_number):
        if phone_number.data != current_user.phone_number:
            user = User.query.filter_by(phone_number=phone_number.data).first()
            if user:
                raise ValidationError("Phone number already exists!")
pickup = {"9:00 am","10:00 am","11:00 am","12:00 pm","1:00 pm","2:00 pm","3:00 pm","4:00 pm"}

delivery= {"10:00 am","10:10 am","10:20 am","10:30 am","10:40 am","10:50 am",
           "11:00 am","11:10 am","11:20 am","11:30 am","11:40 am","11:50 am",
           "12:00 pm","12:10 pm","12:20 pm","12:30 pm","12:40 pm","12:50 pm",
           "1:00 pm","1:10 pm","1:20 pm","1:30 pm","1:40 pm","1:50 pm",
           "2:00 pm","2:10 pm","2:20 pm","2:30 pm","2:40 pm","2:50 pm",
           "3:00 pm","3:10 pm","3:20 pm","3:30 pm","3:40 pm","3:50 pm",
           "4:00 pm","4:10 pm","4:20 pm","4:30 pm","4:40 pm","4:50 pm"}



class NewOrderForm(FlaskForm):

    product_6l_round = IntegerField("6l round", validators=[DataRequired()], default=0)
    product_5g_round = IntegerField("5g round", validators=[DataRequired()])
    product_5g_slim = IntegerField("5g slim", validators=[DataRequired()])
    is_delivery = BooleanField("For Deliver?", validators=[DataRequired()])
    time_pickup = SelectField("Pickup Time", coerce=str ,validators=[DataRequired()])
    time_delivery = SelectField("Delivery Time", choices=(""),validators=[DataRequired()])
    submit = SubmitField("Order")







