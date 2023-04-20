class Account:
    """
    A class that represents a bank account.

    Methods:
    -----------
    __init__(name: str) -> None
        Initializes an Account object with the given name and sets the balance to 0.

    deposit(amount: float) -> bool
        Deposits the specified amount into the account if it is positive and returns True. 
        Otherwise, returns False.

    withdraw(amount: float) -> bool
        Withdraws the specified amount from the account if it is positive and less than or equal to 
        the account balance, and returns True. Otherwise, returns False.

    get_balance() -> float
        Returns the current balance of the account.

    get_name() -> str
        Returns the name associated with the account.
    """
    def __init__(self, name: str) -> None:
        """
        Initializes an Account object with the given name and sets the balance to 0.

        Parameters:
        -----------
        name : str
            The name associated with the account.
        """
        self.__account_name = name
        self.__account_balance = float(0)

    def deposit(self, amount: float) -> bool:
        """
        Deposits the specified amount into the account if it is positive and returns True. 
        Otherwise, returns False.

        Parameters:
        -----------
        amount : float
            The amount to deposit into the account.

        Returns:
        --------
        bool
            True if the deposit was successful, False otherwise.
        """
        try:
            if (amount > 0):
                self.__account_balance += float(amount)
                return True
            elif (amount <= 0):
                raise(ValueError)
        except:
            return False
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraws the specified amount from the account if it is positive and less than or equal to 
        the account balance, and returns True. Otherwise, returns False.

        Parameters:
        -----------
        amount : float
            The amount to withdraw from the account.

        Returns:
        --------
        bool
            True if the withdrawal was successful, False otherwise.
        """
        try:
            if (amount > 0 and amount <= self.__account_balance):
                self.__account_balance -= float(amount)
                return True
            elif (amount <= 0 or amount > self.__account_balance):
                raise(ValueError)
        except:
            return False
    
    def get_balance(self) -> float:
        """
        Returns the current balance of the account.

        Returns:
        --------
        float
            The current balance of the account.
        """
        return self.__account_balance
    
    def get_name(self) -> str:
        """
        Returns the name associated with the account.

        Returns:
        --------
        str
            The name associated with the account.
        """
        return self.__account_name
