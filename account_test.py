import unittest
from unittest.mock import Mock

from banking import (
    Account,
    Console,
    TransactionRepository,
    StatementPrinter,
    Clock,
)


class AccountShould(unittest.TestCase):
    _clock: Clock = Clock()
    _transaction_repository: TransactionRepository = TransactionRepository(_clock)
    _transaction_repository.add_deposit: Mock = Mock()
    _transaction_repository.add_withdrawal: Mock = Mock()
    _console: Console = Console()
    _statement_printer: StatementPrinter = StatementPrinter(_console)
    _statement_printer.print: Mock = Mock()

    _account = Account(_transaction_repository, _statement_printer)

    def test_store_a_deposit_transaction(self):
        self._account.deposit(100)
        self._transaction_repository.add_deposit.assert_called_once_with(100)

    def test_store_a_withdrawal_transaction(self):
        self._account.withdraw(100)
        self._transaction_repository.add_withdrawal.assert_called_once_with(100)

    def test_print_a_statement(self):
        self.assertIsInstance(self._transaction_repository.all_transactions(), list)
        self._account.print_statement()
        self._statement_printer.print.assert_called_once()


if __name__ == "__main__":
    unittest.main()
