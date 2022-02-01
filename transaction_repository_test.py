import unittest
from unittest.mock import Mock, call

from banking import (
    Account,
    Console,
    TransactionRepository,
    StatementPrinter,
    Transaction,
    Clock,
)


class TransactionRepositoryShould(unittest.TestCase):
    _clock: Clock = Clock()

    def test_create_and_store_a_deposit_transaction(self):
        _transaction_repository: TransactionRepository = TransactionRepository(
            self._clock
        )
        self._clock.today_as_string = Mock(return_value="12/05/2015")
        _transaction_repository.add_deposit(100)

        transactions = _transaction_repository.all_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0], Transaction("12/05/2015", 100))

    def test_create_and_store_a_withdrawal_transaction(self):
        _transaction_repository: TransactionRepository = TransactionRepository(
            self._clock
        )
        self._clock.today_as_string = Mock(return_value="12/05/2015")
        _transaction_repository.add_withdrawal(100)

        transactions = _transaction_repository.all_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0], Transaction("12/05/2015", -100))


if __name__ == "__main__":
    unittest.main()
