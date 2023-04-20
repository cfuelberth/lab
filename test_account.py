import pytest
from account import Account

def test_deposit():
    account = Account('John Doe')
    assert account.deposit(100) == True
    assert account.get_balance() == 100

def test_deposit_negative_amount():
    account = Account('John Doe')
    assert account.deposit(-100) == False
    assert account.get_balance() == 0

def test_withdraw():
    account = Account('John Doe')
    account.deposit(100)
    assert account.withdraw(50) == True
    assert account.get_balance() == 50

def test_withdraw_negative_amount():
    account = Account('John Doe')
    account.deposit(100)
    assert account.withdraw(-50) == False
    assert account.get_balance() == 100

def test_withdraw_greater_than_balance():
    account = Account('John Doe')
    account.deposit(100)
    assert account.withdraw(200) == False
    assert account.get_balance() == 100
    
def test_get_name():
    account = Account('John Doe')
    assert account.get_name() == 'John Doe'