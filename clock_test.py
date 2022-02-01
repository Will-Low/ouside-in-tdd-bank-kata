import datetime
import unittest

from banking import Clock


class ClockShould(unittest.TestCase):
    class TestableClock(Clock):
        _today = datetime.date.fromisoformat("2015-04-24")

    def test_todays_date_in_dd_MM_yyyy_format(self):
        clock = self.TestableClock()
        date = clock.today_as_string()
        self.assertEqual(date, "24/04/2015")


if __name__ == "__main__":
    unittest.main()
