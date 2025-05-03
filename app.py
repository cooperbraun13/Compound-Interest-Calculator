from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None

    if request.method == 'POST':
        # Get values from form
        principal = float(request.form.get('principal', 0))
        rate = float(request.form.get('rate', 0)) / 100
        time = float(request.form.get('time', 0))
        compounds = int(request.form.get('compounds', 1))
        
        # Calculate compound interest
        amount = principal * (1 + rate/compounds)**(compounds*time)
        interest = amount - principal
        
        result = {
            'principal': principal,
            'rate': rate * 100,
            'time': time,
            'compounds': compounds,
            'amount': amount,
            'interest': interest
        }
    
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
