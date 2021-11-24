class Password:
    def ValidPassword(self, password):

        r"""
        >>> p = Password()
        >>> p.ValidPassword("")
        False
        >>> p.ValidPassword("Has1*")
        False
        >>> p.ValidPassword("haslo.bez.duzej.litery123")
        False
        >>> p.ValidPassword("Haslo.bez.liczby")
        False
        >>> p.ValidPassword("HasloBezZnaku123")
        False
        >>> p.ValidPassword("haslotylkozliczba123")
        False
        >>> p.ValidPassword("HasloTylkoZDuzaLitera")
        False
        >>> p.ValidPassword("haslo.tylko.z.znakiem")
        False
        >>> p.ValidPassword("Prawidlowe.Haslo123")
        True
        """

        numbersaray = ['0','1','2','3','4','5','6','7','8','9']
        numbers = 0

        if type(password) != str:
            raise Exception('Wrong type.')
        if len(password) < 8:
            return False
        if password.lower() == password:
            return False
        if password.isalnum():
            return False
        for i in range(0, len(numbersaray)):
            if password.find(numbersaray[i]) != -1:
                numbers += 1
        if numbers == 0:
            return False
        return True


import unittest

class PasswordTest(unittest.TestCase):

    def setUp(self):
        self.temp = Password()

    def test_Password_Exceptions_None(self):
        self.assertRaises(Exception, self.temp.ValidPassword, None)
    def test_Password_Exceptions_Boolean(self):
        self.assertRaises(Exception, self.temp.ValidPassword, True)
    def test_Password_Exceptions_int(self):
        self.assertRaises(Exception, self.temp.ValidPassword, 2)
    def test_Password_Exceptions_float(self):
        self.assertRaises(Exception, self.temp.ValidPassword, 2.5)
    def test_Password_Exceptions_array(self):
        self.assertRaises(Exception, self.temp.ValidPassword, [1,2,3])
    def test_Password_Exceptions_object(self):
        self.assertRaises(Exception, self.temp.ValidPassword, {})
        
    def tearDown(self):
        self.temp = None 


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    unittest.main()

