import unittest
from unittest.mock import Mock, call

from banking import (
    Account,
    Console,
    TransactionRepository,
    StatementPrinter,
    Clock,
)


class PrintStatementTest(unittest.TestCase):
    _console: Console = Console()
    _console.print_line: Mock = Mock()
    _clock: Clock = Clock()
    _clock.today_as_string: Mock = Mock()
    _clock.today_as_string.side_effect = ["01/04/2014", "02/04/2014", "10/04/2014"]
    _transaction_repository: TransactionRepository = TransactionRepository(_clock)
    _statement_printer: StatementPrinter = StatementPrinter(_console)
    _account: Account = Account(_transaction_repository, _statement_printer)

    def test_print_statement_containing_all_transactions(self):
        self._account.deposit(1000)
        self._account.withdraw(100)
        self._account.deposit(500)
        self._account.print_statement()

        lines = [
            "DATE | AMOUNT | BALANCE",
            "10/04/2014 | 500.00 | 1400.00",
            "02/04/2014 | -100.00 | 900.00",
            "01/04/2014 | 1000.00 | 1000.00",
        ]

        calls = [call(line) for line in lines]

        self._console.print_line.assert_has_calls(calls)


if __name__ == "__main__":
    unittest.main()
