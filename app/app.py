from flask import Flask, render_template, request
import math
import re

app = Flask(__name__)

def tokenize(expression): 
    # 数字（整数・小数）と演算子を分けてリスト化
    return re.findall(r'sqrt|\d+\.?\d*|[+\-*/^()]', expression)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "エラー: ゼロで割ることはできません"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "エラー: 負の数の平方根は計算できません"
    return math.sqrt(x)

def calculate(expression):
    # tokens = expression.split()
    tokens = tokenize(expression)

    if len(tokens) == 3:
        x, operator, y = tokens
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            return "エラー: 数値ではない値が入力されています"

        if operator == "+":
            return add(x, y)
        elif operator == "-":
            return subtract(x, y)
        elif operator == "*":
            return multiply(x, y)
        elif operator == "/":
            return divide(x, y)
        elif operator == "^":
            return power(x, y)
        else:
            return "エラー: サポートされていない演算子です"

    elif len(tokens) == 2 and tokens[0] == "sqrt":
        try:
            x = float(tokens[1])
            return sqrt(x)
        except ValueError:
            return "エラー: 数値ではない値が入力されています"

    return "エラー: 不正な入力"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        expression = request.form["expression"]
        result = calculate(expression)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50)