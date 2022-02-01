import unittest
from unittest.mock import Mock, call

from banking import (
    Account,
    Console,
    TransactionRepository,
    StatementPrinter,
    Transaction,
)


class AccountShould(unittest.TestCase):
    _transaction_repository: TransactionRepository = TransactionRepository()
    _transaction_repository.add_deposit: Mock = Mock()
    _transaction_repository.add_withdrawal: Mock = Mock()
    _statement_printer: StatementPrinter = StatementPrinter()
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
