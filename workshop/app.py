# coding=utf-8
import logging

from flask import Flask, request
from flask_cors import CORS

logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def hello_world():
    """
    :return: "Hello, world!" til de som besøker siden. 
    """
    return "Hello, World!"


@app.route('/calculator', methods=['GET'])
def calculator():
    """
    Operatorer og operand er angitt i query-parametrene "operator", "operand1" og "operand2", 
    f.eks /greet?operator=plus&operand1=2&operand2=2
    Endepunktet skal støtte "plus", "minus", "mult" og "div".
    :return: Resultatet av enkle heltallsoperasjoner.
    """
    op = request.args.get('operator')
    op1 = float(request.args.get('operand1'))
    op2 = float(request.args.get('operand2'))
    if op == "plus":
        return "Sum of %.2f and %.2f is %.2f" % (op1, op2, op1 + op2)
    elif op == "minus":
        return "Difference of %.2f and %.2f is %.2f" % (op1, op2, op1 - op2)
    elif op == "mult":
        return "Product of %.2f and %.2f is %.2f" % (op1, op2, op1 * op2)
    elif op == "div":
        return "Quotient of %.2f and %.2f is %.2f" % (op1, op2, op1 / op2)
    else:
        return ("Invalid operator: %s" % op), 400


if __name__ == '__main__':
    app.run()
