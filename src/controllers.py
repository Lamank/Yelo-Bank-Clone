from flask import render_template, redirect, request
from models import *
from exchange import exchange
from app import *
from forms import *
from werkzeug.utils import secure_filename
from extensions import share
import os



@app.route("/")
def home():
    
    news = News.query.order_by(News.added_at.desc())[:3]
    return render_template("index.html", all_news = news, exchange = exchange, status=True)


@app.route("/az/news/")
def news():
    
    news = News.query.order_by(News.added_at.desc())
    return render_template("news.html", all_news=news)



    

@app.route("/az/news/<slug>/")
def news_details(slug):
    news = News.query.filter_by(slug=slug).first()
    content= news.content.split("\n")
    return render_template("news_details.html",title = news.title, content=content, image=news.image_url, adding= news.added_at)



@app.route("/individuals/cards/")
def cards():
    cards = Card.query.all()
    for card in cards:

        print(card.id)
    return render_template('cards.html', cards=cards,  status = True)


@app.route("/individuals/cards/<string:card_type>/", methods=['GET', 'POST'])
def card_detailed(card_type):
    if card_type == 'yelo-kart-debet':
        check = '1'
    elif card_type == 'yelo-kart-premium':
        check = '2'
    elif card_type == 'yelo-loan-card':
        check = '3'
    print(card_type)
    post_data = request.form
    form = CardRequestForm()
    if request.method == 'POST':
        form = CardRequestForm(data=post_data)
        if form.validate_on_submit():
            file1_data = form.file1.data
            file2_data = form.file2.data
            file1_data.save(os.path.join(os.path.abspath(os.path.dirname(
                __file__)), app.config['UPLOAD_FOLDER'], secure_filename(file1_data.filename)))
            file2_data.save(os.path.join(os.path.abspath(os.path.dirname(
                __file__)), app.config['UPLOAD_FOLDER'], secure_filename(file2_data.filename)))
            card = Cardreq(cardtype=form.cardtype.data, val=form.val.data, first_name=form.first_name.data,
                           last_name=form.last_name.data, prefiks=form.prefiks.data, phone=form.phone.data, code_word=form.code_word.data, branch=form.branch.data, file1=form.file1.data, file2=form.file2.data)
            card.save()
            return redirect("/success/success-loan-request/")
    card = Card.query.filter(Card.id == check).first()
    main_features = Feature.query.filter(Feature.card_id == check, Feature.type == 'main').all()
    additional_features = Feature.query.filter(Feature.card_id == check, Feature.type == 'additional').all()
    return render_template('detailed-card.html', card=card,  main_features = main_features, additional_features = additional_features, form=form, status=True)


@app.route("/individuals/deposits/")
def deposits():
    deposits = Deposit.query.all()
    return render_template('deposits.html', deposits=deposits, status=True)


@app.route("/individuals/online-services/loan_request/", methods=['GET', 'POST'])
def loan_request():
    post_data = request.form
    form = LoanRequestForm()
    if request.method == 'POST':
        form = LoanRequestForm(data=post_data)
        if form.validate_on_submit():
            loan = Loanreq(salary=form.salary.data, loan=form.loan.data, first_name=form.first_name.data,
                           last_name=form.last_name.data, workplace=form.workplace.data, prefiks=form.prefiks.data, phone=form.phone.data)
            loan.save()
            return redirect("/success/success-loan-request/")
    return render_template('online-services.html', form=form)


@app.route("/success/success-loan-request/")
def success():
    return render_template("success-loan-request.html")

