import unittest
from unittest.mock import Mock, call

from banking import (
    Account,
    Console,
    TransactionRepository,
    StatementPrinter,
    Transaction,
)
