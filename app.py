import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        age = request.form["age"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(age),
            temperature=0.8,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(age):
    return """Juno Provide benefits that enable employees to show up as the best version of themselves: happier, healthier and more engaged.
Employees can choose from over 500+ curated experiences that support their wellbeing. Some of the categories it provides benefits
are Workshops, Flower Delivery, Healthy Eating, Skincare Products, Meals Kit, Fitness Apps, Spa Treatments.
Recommend the benefits which employees in India would want based on their age  
Age: 21
Benefits: Udemy Credits, Audible Subscription, Netflix Subscription, Zomato Discount Codes, RedBus Discount Codes
Age: 23
Benefits: Udemy Credits, Ink42 Subscription, Netflix Subscription, Zomato Discount Codes, Trivago Discount Codes
Age: 25
Benefits: ClearTax Credits, Ink42 Subscription, Captable Subscription, Furlanco Discount Codes, BookMyShow Discount Codes, Socials Discount Coupons
Age: 27
Benefits: Nyka Credits, Myntra Credits, Ajio Credits, Ink42 Subscription, Captable Subscription, Furlanco Discount Codes, BookMyShow Discount Codes, Socials Discount Coupons
Age: 30
Benefits: Nyka Credits, UpGrad Credits, FirstCry Credits, Ink42 Subscription, UrbanCompany Subscription, Furlanco Discount Codes, BookMyShow Discount Codes
Age:{}
Benefits:""".format(
        age
    )



