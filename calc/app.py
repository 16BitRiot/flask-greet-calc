from flask import Flask, request, redirect
app = Flask(__name__)

def perform_operation(operation, input1, input2):
    input1 = float(input1)
    input2 = float(input2)
    if operation == 'add':
        return f'{input1} + {input2}', input1 + input2
    elif operation == 'subtract':
        return f'{input1} - {input2}', input1 - input2
    elif operation == 'multiply':
        return f'{input1} * {input2}', input1 * input2
    elif operation == 'divide':
        return f'{input1} / {input2}', input1 / input2

@app.route("/")
def hello():
    return """
        <body>
        <h1>Welcome!</h1>
        <form>
            <button type="submit" formaction="/calc">Click here for Calculator!</button>
        </form>
        </body>
    """


@app.route('/calc', methods=["GET", "POST"])
def calculator():
    if request.method == 'POST':
        input1 = request.form["input1"]
        input2 = request.form["input2"]
        operation = request.form["operation"]
        # call the function in operations.py to perform the calculation
        equation, result = perform_operation(operation, input1, input2)
        return redirect(f'/calc?equation={equation}&result={result}')
    equation = request.args.get('equation')
    result = request.args.get('result')
    return f"""
        <body>
        <h1>Simple Calculator</h1>
        <form method="POST" action="/calc">
            <input type="text" placeholder="Input 1" name="input1">
            <input type="text" placeholder="Input 2" name="input2">
            <select name="operation">
                <option value="add">Add</option>
                <option value="subtract">Subtract</option>
                <option value="multiply">Multiply</option>
                <option value="divide">Divide</option>
            </select>
            <button>Calculate</button>
        </form>
        <p>Equation: {equation}</p>
        <p>Result: {result}</p>
        """

if __name__ == '__main__':
    app.run()