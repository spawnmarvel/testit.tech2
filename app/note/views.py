"""___"""
import random
import string
import datetime
import logging

from flask import render_template, request, redirect, url_for, session, flash
from flask_login import login_required
# internal
from app.db import db_handler

from . import note


@note.route("/noteview")
def note_view():
    note_data = db_handler.db_all_note()
    result = "Null"
    secret = "Null"
    if request.method == 'POST':
        return render_template("note/notes_view.html", note_data=note_data, result=result, secret=secret)
    # get
    return render_template("note/notes_view.html", note_data=note_data, result=result, secret=secret)
    

@note.route("/noteadmin", methods=['GET', 'POST'])
@login_required
def notes_db():
    note_data = db_handler.db_all_note()
    secret = "use same as password, or make a secret word"
    current_time = datetime.datetime.now()
    if request.method == 'POST':
        if request.form["action"] == "Add":
            #db logger add
            note = request.form["nt"]
            # level_ = request.form["options"]
            topic_url = request.form["url"]
            # drop = request.form["drop_option"]
            topic = request.form["selectvalue"]
            if len(note) < 5 or len(topic_url) < 6:
                result = "Note must be > 5 and url must be > 6"
            else:
                db_handler.db_insert_note()
                # result = sqlalchemy_statments.insert(note, topic, topic_url)
                # result += " topic: " + str(topic)
        elif request.form["action"] == "DeleteNote":
                # logger.info("delete note")
                del_pa_ = "master"
                tmp_del_pa_ = request.form["delpass"]
                print(format(tmp_del_pa_))
                print(format(del_pa_))
                if tmp_del_pa_.lower() == del_pa_:
                    notes_id = request.form["delid"]
                    # result = sqlalchemy_statments.delete(notes_id)
                    db_handler.db_delete_note()

                    num_1 = random.randint(0, 333)
                    num_2 = random.randint(0, 99)
                    letters_1 = random.choice(string.ascii_letters)
                    letters_2 = random.choice(string.ascii_letters)
                    result += "  KEY" +  letters_1 + str(num_1) + letters_2 + str(num_2)
                    secret = " Success"
                else:
                    result = "Secret key is wrong"
                    secret = "Secret key is wrong"
        else:
            pass
    else:
        result = "GET: " + str(current_time)
           
        return render_template("note/notes.html", note_data=note_data, result=result, secret=secret)

    return render_template("note/notes.html", note_data=note_data, result=result, secret=secret)



