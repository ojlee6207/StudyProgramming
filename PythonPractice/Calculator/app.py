from flask import Flask, request, render_template
from calculator import parse_expression, calculate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        command = request.form.get("expression")
        try:
            num1, operator, num2 = parse_expression(command)
            result = calculate(num1,operator,num2)
        except Exception:
            result = "계산 오류"
    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)