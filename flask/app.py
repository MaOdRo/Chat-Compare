from flask import Flask, request, render_template, redirect
from csv import writer
from datetime import datetime as dt
from gptbot import answerMeWatches, answerMeWecker

def add_info(tic_id, chatbot_name, interaction_date):
    row = [tic_id, chatbot_name, interaction_date]
    #in csv eintragen
    with open('master_data.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(row)
        #schließen?
        f_object.close()

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template("index.html")

######GPT BOTS###########

#Uhren

@app.route('/botwatches')
def botwatches():
    user_id = request.args.get('tic')
    bot_name = "Chronos[LuxusChatGBT]"
    interaction_date = dt.now()
    add_info(user_id, bot_name, interaction_date)

    return render_template("watches.html", variable=user_id)

@app.route("/get_watch", methods=["GET","POST"])
def chatbot_response_uhr():
    msg = request.form["msg"]
    response = answerMeWatches(msg)
    return str(response)

#Wecker

@app.route('/botwecker')
def botwecker():
    user_id = request.args.get('tic')
    bot_name = "Janus[WeckerChatGBT]"
    interaction_date = dt.now()
    add_info(user_id, bot_name, interaction_date)

    return render_template("wecker.html", variable=user_id)

@app.route("/get_wecker", methods=["GET","POST"])
def chatbot_response_wecker():
    msg = request.form["msg"]
    response = answerMeWecker(msg)
    return str(response)



#######RASA BOTS###########

@app.route("/rasawatches", methods=["GET","POST"])
def rasawatch():
    user_id = request.args.get('tic') 
    bot_name = "Kairos[LuxusRasa]"
    interaction_date = dt.now()
    add_info(user_id, bot_name, interaction_date)
    return render_template('rasawatches.html', variable=user_id)


@app.route("/rasawecker", methods=["GET","POST"])
def rasawecker():
    user_id = request.args.get('tic') 
    bot_name = "Aion[WeckerRasa]"
    interaction_date = dt.now()
    add_info(user_id, bot_name, interaction_date)
    return render_template('rasawecker.html', variable=user_id)




######Rerouting###########

@app.route('/redirectunipark', methods=["GET"])
def redirectunipark():
    #user_id = request.args.get('return_tic')
    request_parameter = request.query_string.decode('utf-8')
    #url = "https://ww2.unipark.de/uc/Masterarbeiten/988e/ospe.php?{0}".format(request_parameter)
    url = "https://ww2.unipark.de/uc/Masterarbeiten/a51b/ospe.php?{0}".format(request_parameter)
    return redirect(url)