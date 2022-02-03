import unittest
from unittest.mock import Mock

from banking import (
    TransactionRepository,
    Transaction,
    Clock,
)


class TransactionRepositoryShould(unittest.TestCase):
    def test_create_and_store_a_deposit_transaction(self):
        clock: Clock = Clock()
        transaction_repository: TransactionRepository = TransactionRepository(clock)
        clock.today_as_string = Mock(return_value="12/05/2015")
        transaction_repository.add_deposit(500)

        transactions = transaction_repository.all_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0], Transaction("12/05/2015", 500))

    def test_create_and_store_a_withdrawal_transaction(self):
        clock: Clock = Clock()
        transaction_repository = TransactionRepository(clock)
        clock.today_as_string = Mock(return_value="13/05/2015")
        transaction_repository.add_withdrawal(100)

        transactions = transaction_repository.all_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0], Transaction("13/05/2015", -100))


if __name__ == "__main__":
    unittest.main()
