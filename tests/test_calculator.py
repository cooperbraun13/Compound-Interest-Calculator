import pytest
from flask import Flask
from app.calculator import calculate_compound_interest
from app import create_app

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """
    Test that homepage loads correctly.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b'Compound Interest Calculator' in response.data

def test_form_submission(client):
    """
    Test that form submission works.
    """
    response = client.post('/', data={
        'principal': 1000,
        'rate': 5,
        'time': 5,
        'compounds': 12
    })
    assert response.status_code == 200
    assert b'Your Investment Results' in response.data

def test_basic_calculation():
    """
    Test a basic compound interest calculation.
    """
    result = calculate_compound_interest(1000, 5, 5, 12)
    assert round(result['amount'], 2) == 1283.36
    assert round(result['interest'], 2) == 283.36

def test_zero_principal():
    """
    Test calculation with zero principal.
    """
    result = calculate_compound_interest(0, 5, 5, 12)
    assert result['amount'] == 0
    assert result['interest'] == 0

def test_zero_rate():
    """
    Test calculation with zero interest rate.
    """
    result = calculate_compound_interest(1000, 0, 5, 12)
    assert result['amount'] == 1000
    assert result['interest'] == 0

def test_zero_time():
    """
    Test calculation with zero time period.
    """
    result = calculate_compound_interest(1000, 5, 0, 12)
    assert result['amount'] == 1000
    assert result['interest'] == 0

def test_annual_compounding():
    """
    Test calculation with annual compounding.
    """
    result = calculate_compound_interest(1000, 5, 5, 1)
    assert round(result['amount'], 2) == 1276.28
    assert round(result['interest'], 2) == 276.28

def test_continuous_compounding():
    """
    Test calculation with many compounding periods (approximating continuous).
    """
    result = calculate_compound_interest(1000, 5, 5, 365)
    # Compare with a high compounding frequency
    assert round(result['amount'], 2) == 1284.03
    assert round(result['interest'], 2) == 284.03

def test_high_interest_rate():
    """
    Test calculation with a high interest rate.
    """
    result = calculate_compound_interest(1000, 20, 5, 12)
    assert round(result['amount'], 2) == 2713.49
    assert round(result['interest'], 2) == 1713.49

def test_long_time_period():
    """
    Test calculation with a long time period.
    """
    result = calculate_compound_interest(1000, 5, 30, 12)
    assert round(result['amount'], 2) == 4467.74
    assert round(result['interest'], 2) == 3467.74