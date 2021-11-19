import unittest
from Zad3 import statement
invoice = {
    "customer": "BigCo",
    "performances": [
      {
        "playID": "as-like",
        "audience": 35
      }
    ]
}
plays = {
    "hamlet": {"name": "Hamlet", "type": "tragedy"},
    "as-like": {"name": "As You Like It", "type": "comedy"},
    "othello": {"name": "Othello", "type": "tragedy"}
}
class StatementTest(unittest.TestCase):

    def test_Statement_comedy(self):
        self.assertEqual(statement(invoice, plays), 
        "Statement for BigCo\n As You Like It: $580.00 (35 seats)\nAmount owed is $580.00\nYou earned 12 credits\n")

    def test_Statement_Error(self):
        self.assertRaises(ValueError, statement, invoice, {"as-like": {"name": "As You Like It", "type": "wrongtype"}})

