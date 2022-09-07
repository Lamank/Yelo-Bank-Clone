from extensions import db, admin
from flask_admin.contrib.sqla import ModelView
from app import app
from datetime import date
from slugify import slugify, Slugify
from flask import session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert
from extensions import *
from app import *
from datetime import *


class News(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    image_url = db.Column(db.Text(), nullable = False)
    added_at = db.Column(db.Date(), nullable = False)
    slug = db.Column(db.String(255), nullable = True)
    
    def __repr__(self):
        return self.title

    def create_slug(self, title):
        
        my_slug = Slugify()
        my_slug.pretranslate = {'ə': 'e', 'ü': 'u', 'ğ':'g', 'ş':'sh', 'ç':'ch'}
        my_slug.to_lower = True
        my_slug.max_length = 35
        return my_slug(title)

    def __init__(self, title, content, image_url):
        self.title = title
        self.content = content
        self.image_url = image_url
        self.added_at = date.today().strftime("%Y-%m-%d")
        self.slug = self.create_slug(title)

    def save(self):
        db.session.add(self)
        db.session.commit()


class Loanreq(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    salary = db.Column(db.Integer())
    loan = db.Column(db.Integer())
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    workplace = db.Column(db.String(200))
    prefiks = db.Column(db.Integer())
    phone = db.Column(db.Integer())

    def __repr__(self):
        return self.title

    def __init__(self, salary, loan, first_name, last_name, workplace, prefiks, phone):
        self.salary = salary
        self.loan = loan
        self.first_name = first_name
        self.last_name = last_name
        self.workplace = workplace
        self.prefiks = prefiks
        self.phone = phone

    def save(self):
        db.session.add(self)
        db.session.commit()


class Cardreq(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    cardtype = db.Column(db.String(200))
    val = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    prefiks = db.Column(db.Integer())
    phone = db.Column(db.Integer())
    code_word = db.Column(db.String(200))
    branch = db.Column(db.String(200))
    file1 = db.Column(db.String(200))
    file2 = db.Column(db.String(200))

    def __repr__(self):
        return self.title

    def __init__(self, cardtype, val, first_name, last_name, prefiks, phone, code_word, branch, file1, file2):
        self.cardtype = cardtype
        self.val = val
        self.first_name = first_name
        self.last_name = last_name
        self.prefiks = prefiks
        self.phone = phone
        self.code_word = code_word
        self.branch = branch
        self.file1 = file1
        self.file2 = file2

    def save(self):
        db.session.add(self)
        db.session.commit()


class Deposit(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text(), nullable=True)
    image_url = db.Column(db.String(200))
    feature1 = db.Column(db.String(200))
    feature2 = db.Column(db.String(200))
    feature3 = db.Column(db.String(200))
    feature1_value = db.Column(db.String(200))
    feature2_value = db.Column(db.String(200))
    feature3_value = db.Column(db.String(200))

    def __repr__(self):
        return self.title

    def __init__(self, title, description, image_url, feature1, feature2, feature3, feature1_value, feature2_value, feature3_value):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.feature1 = feature1
        self.feature2 = feature2
        self.feature3 = feature3
        self.feature1_value = feature1_value
        self.feature2_value = feature2_value
        self.feature3_value = feature3_value

    def save(self):
        db.session.add(self)
        db.session.commit()




class Card(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text(), nullable=True)
    image_url = db.Column(db.String(200))
    feature1 = db.Column(db.String(200))
    feature2 = db.Column(db.String(200))
    feature3 = db.Column(db.String(200))
    feature1_value = db.Column(db.String(200))
    feature2_value = db.Column(db.String(200))
    feature3_value = db.Column(db.String(200))
    detailed_description = db.Column(db.Text(), nullable=True)
    imp_note = db.Column(db.String(200))
    second_desc_title = db.Column(db.Text())
    second_desc = db.Column(db.Text())
    second_features_title = db.Column(db.Text())
    card_type = db.Column(db.String(50))

    def __repr__(self):
        return self.title

    def __init__(self, title, description, image_url, feature1, feature2, feature3, feature1_value, feature2_value, feature3_value, detailed_description, imp_note, second_desc_title, second_desc, second_features_title, card_type ):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.feature1 = feature1
        self.feature2 = feature2
        self.feature3 = feature3
        self.feature1_value = feature1_value
        self.feature2_value = feature2_value
        self.feature3_value = feature3_value
        self.detailed_description = detailed_description
        self.imp_note = imp_note
        self.second_desc_title = second_desc_title
        self.second_desc = second_desc
        self.second_features_title = second_features_title
        self.card_type=card_type

    def save(self):
        db.session.add(self)
        db.session.commit()



class Feature(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    image_url = db.Column(db.String(200))
    title = db.Column(db.String(200))
    second_title = db.Column(db.String(2000))
    type = db.Column(db.String(200))
    card_id = db.Column(db.Integer(), db.ForeignKey(Card.id))

    def __repr__(self):
        return self.title

    def __init__(self, image_url, title,second_title, type, card_id):
        self.image_url = image_url
        self.title = title
        self.second_title = second_title
        self.type = type
        self.card_id = card_id

    def save(self):
        db.session.add(self)
        db.session.commit()




admin.add_view(ModelView(News, db.session))
admin.add_view(ModelView(Card, db.session))
admin.add_view(ModelView(Deposit, db.session))
admin.add_view(ModelView(Loanreq, db.session))
admin.add_view(ModelView(Feature, db.session))
admin.add_view(ModelView(Cardreq, db.session))
