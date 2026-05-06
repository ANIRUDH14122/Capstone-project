from flask import Flask, render_template, request, redirect

app = Flask(__name__)

transactions = []


@app.route("/")
def home():

    income = 0
    expense = 0

    for item in transactions:

        amount = float(item["amount"])

        if item["type"] == "Income":
            income += amount
        else:
            expense += amount

    balance = income - expense

    return render_template(
        "index.html",
        transactions=transactions,
        income=income,
        expense=expense,
        balance=balance
    )


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        transactions.append({
            "amount": request.form["amount"],
            "category": request.form["category"],
            "type": request.form["type"]
        })

        return redirect("/")

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)