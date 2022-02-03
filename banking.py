import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class Transaction:
    date: str
    amount: int


class Clock:
    _today = datetime.date.today()

    def today_as_string(self):
        return self._today.strftime("%d/%m/%Y")


class TransactionRepository:
    def __init__(self, clock: Clock):
        self._clock = clock
        self._transactions: List[Transaction] = []

    def add_deposit(self, amount: int):
        self._transactions.append(Transaction(self._clock.today_as_string(), amount))

    def add_withdrawal(self, amount: int):
        self._transactions.append(
            Transaction(self._clock.today_as_string(), amount * -1)
        )

    def all_transactions(self) -> List[Transaction]:
        return self._transactions


class Console:
    def print_line(self, text: str):
        raise NotImplementedError


class StatementPrinter:
    _STATEMENT_HEADER: str = "DATE | AMOUNT | BALANCE"

    def __init__(self, console: Console):
        self._console: Console = console

    def print(self, transactions: List[Transaction]):
        self._console.print_line(self._STATEMENT_HEADER)

        prep_for_running_balance_calculation(transactions)

        transactions_with_running_balance = tie_transaction_to_running_balance(transactions)

        order_transactions_for_statement_printing(transactions_with_running_balance)

        for t in transactions_with_running_balance:
            self._console.print_line(f"{t[0].date} | {t[0].amount:.2f} | {t[1]:.2f}")


def prep_for_running_balance_calculation(transactions: List[Transaction]):
    transactions.sort(key=lambda t: datetime.datetime.strptime(t.date, "%d/%m/%Y"))

def tie_transaction_to_running_balance(transactions: List[Transaction]):
    running_balance = 0
    transactions_with_running_balance = []
    for t in transactions:
        running_balance += t.amount
        transactions_with_running_balance.append((t, running_balance))
    return transactions_with_running_balance

def order_transactions_for_statement_printing(transactions: List[Transaction]):
    transactions.reverse()

# Per kata rules, adjusting public methods is not allowed
class Account:
    def __init__(
        self,
        transaction_repository: TransactionRepository,
        statement_printer: StatementPrinter,
    ):
        self._transaction_repository = transaction_repository
        self._statement_printer = statement_printer

    def deposit(self, amount: int):
        self._transaction_repository.add_deposit(amount)

    def withdraw(self, amount: int):
        self._transaction_repository.add_withdrawal(amount)

    def print_statement(self):
        self._statement_printer.print(self._transaction_repository.all_transactions())
