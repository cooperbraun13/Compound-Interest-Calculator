from flask import Blueprint, render_template, request

bp = Blueprint('calculator', __name__, url_prefix='/')

def calculate_compound_interest(principal, rate, time, compounds):
    """
    Calculate compound interest with the given parameters.
    """
    rate = rate / 100  # Convert percentage to decimal
    amount = principal * (1 + rate/compounds)**(compounds*time)
    interest = amount - principal
    
    return {
        'principal': principal,
        'rate': rate * 100,
        'time': time,
        'compounds': compounds,
        'amount': amount,
        'interest': interest
    }

@bp.route('/', methods=['GET', 'POST'])
def calculator():
    result = None

    if request.method == 'POST':
        # Get values from form
        principal = float(request.form.get('principal', 0))
        rate = float(request.form.get('rate', 0))
        time = float(request.form.get('time', 0))
        compounds = int(request.form.get('compounds', 1))
        
        # Calculate compound interest
        result = calculate_compound_interest(principal, rate, time, compounds)
    
    return render_template('calculator.html', result=result)