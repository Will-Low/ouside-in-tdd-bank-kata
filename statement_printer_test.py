import unittest
from typing import List
from unittest.mock import Mock, call

from banking import Console, StatementPrinter, Transaction


class StatementPrinterTest(unittest.TestCase):
    _NO_TRANSACTIONS: List[Transaction] = []
    _console: Console = Console()
    _console.print_line: Mock = Mock()
    _STATEMENT_HEADER: str = "DATE | AMOUNT | BALANCE"

    def test_always_print_the_header(self):
        statement_printer: StatementPrinter = StatementPrinter(self._console)
        statement_printer.print(self._NO_TRANSACTIONS)
        self._console.print_line.assert_called_with(self._STATEMENT_HEADER)


    def test_print_transactions_in_reverse_chronological_order(self):
        _transactions: List[Transaction] = [
            Transaction("01/04/2014", 1000),
            Transaction("02/04/2014", 100),
            Transaction("10/04/2014", 500)
        ]

        statement_printer: StatementPrinter = StatementPrinter(self._console)
        statement_printer.print(_transactions)

        calls: List[call] = [
            call(self._STATEMENT_HEADER),
            call(_transactions[0]),
            call(_transactions[1]),
            call(_transactions[2]),
        ]

        self._console.print_line.assert_has_calls(calls)

if __name__ == "__main__":
    unittest.main()
