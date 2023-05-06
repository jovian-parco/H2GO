import os
import secrets
from PIL import Image
from H2GO import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from H2GO.forms import RegistrationForm, LoginForm, UpdateAccountForm, NewOrderForm
from H2GO.models import User, Order, Shipment, Product, Time_Pickup, TimeDelivery
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime


@app.route("/")
@app.route("/home")
def home():
    return render_template('public/home.html', title="HOME")


@app.route("/purpose")
def purpose():
    return render_template('public/purpose.html', title="PURPOSE")


@app.route("/goals")
def goals():
    return render_template('public/goals.html', title="GOALS")


@app.route("/order")
@login_required
def order():
    return render_template('public/order.html', title="ORDER")



@app.route("/order/new", methods=["GET", "POST"])
@login_required
def new_order():
    form = NewOrderForm()
    timenow = datetime.now()
    timenow = int(timenow.strftime("%H%M"))
    if timenow <= 2355 and Time_Pickup.query.filter_by(time="0900").first().time_count <= 5:
        time_pickup = {"9:00 am", "10:00 am", "11:00 am", "12:00 pm", "1:00 pm", "2:00 pm", "3:00 pm", "4:00 pm"}
        time_pickup = list(time_pickup)
    else:
        time_pickup = {"shit", "cow"}
        time_pickup = list(time_pickup)
    form.time_pickup.choices = time_pickup
    if form.validate_on_submit():
        flash(f"Order has been Placed!", "success")
        return redirect(url_for("order"))
    return render_template('public/new_order.html', title="ORDER NOW", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data,first_name=form.first_name.data,last_name=form.last_name.data,phone_number=form.phone_number.data,address=form.address.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account Created for {form.username.data}!", "success")
        return redirect(url_for("login"))
    return render_template('public/register.html', title="REGISTER", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash(f"Login Unsuccessful. Check Username & Password", "danger")
    return render_template('public/login.html', title="LOGIN", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

def save_image_file(form_image_file):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext((form_image_file.filename))
    image_file_fn=random_hex+f_ext
    image_file_path=os.path.join(app.root_path,"static/img/profile_img",image_file_fn)
    output_size = (125,124)
    i = Image.open(form_image_file)
    i.thumbnail(output_size)
    i.save(image_file_path)
    return image_file_fn


@app.route("/account_setting",methods=["GET", "POST"])
@login_required
def account_setting():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.image_file.data:
            picture_file=save_image_file(form.image_file.data)
            current_user.image_file = picture_file
        current_user.first_name=form.first_name.data
        current_user.last_name=form.last_name.data
        current_user.phone_number=form.phone_number.data
        current_user.address=form.address.data
        db.session.commit()
        flash(f"Account Has Been Updated", "success")
        return redirect(url_for("account_setting"))
    elif request.method == "GET":
        form.first_name.data=current_user.first_name
        form.last_name.data=current_user.last_name
        form.phone_number.data=current_user.phone_number
        form.address.data=current_user.address
    image_file= url_for("static",filename="img/profile_img/"+ current_user.image_file)
    return render_template('public/account_setting.html', title="ACCOUNT", image_file=image_file,form=form)