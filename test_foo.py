from unittest import main, TestCase, mock
import foo


class TestFoo(TestCase):
    # Function returns an array of substrings from a string, splitted by spaces
    # Does not need mock since the result is fixed and fast
    def test_split_to_list(self):
        self.assertEqual(foo.split_to_list('Hello World'), ['Hello', 'World'])
    
    # Function returns a number from 1 to 6 randomly
    # Need to be mocked since the result is not fixed, which will fail due to randomness of output
    @mock.patch('foo.roll_dice', return_value=6)
    def test_roll_dice(self, mock_roll_dice):
        self.assertEqual(foo.roll_dice(), 6)

    # Function wait for a few seconds, then returns the username
    # Need to be mocked since the result took time, which slows down development
    @mock.patch('foo.fetch_username', return_value='bernardadhitya')
    def test_fetch_username(self, mock_fetch_username):
        self.assertEqual(foo.fetch_username(), 'bernardadhitya')

if __name__ == '__main__':
    main()
