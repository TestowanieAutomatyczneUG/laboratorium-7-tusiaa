class Password:
    def ValidPassword(self, password):
        if type(password) != str:
            raise ValueError('Wrong type.')
        if len(password) < 8:
            raise ValueError('Too short.')








if __name__ == '__main__':
    import doctest
    #doctest.testmod(extraglobs={'p': Password()})


