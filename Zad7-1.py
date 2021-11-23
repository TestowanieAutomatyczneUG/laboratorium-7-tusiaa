class hamming:
    def distance (self, a, b):

        r"""
        >>> h = hamming()
        >>> h.distance("","")
        0
        >>> h.distance("A","A")
        0
        >>> h.distance("G","T")
        1
        >>> h.distance("GGACTGAAATCTG","GGACTGAAATCTG")
        0
        >>> h.distance("GGACGGATTCTG","AGGACGGATTCT")
        9
        >>> h.distance("AATG","AAA")
        Traceback (most recent call last):
            File "C:\Python310\lib\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.hamming.distance[7]>", line 1, in <module>
                h.distance("AATG","AAA")
            File "C:\Users\sleman\Testowanie automatyczne\laboratorium-7-tusiaa\Zad7-1.py", line 41, in distance
            raise ValueError('Wrong value.')
        ValueError: Wrong value.
        >>> h.distance("ATA","AGTG")
        Traceback (most recent call last):
            File "C:\Python310\lib\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.hamming.distance[7]>", line 1, in <module>
                h.distance("ATA","AGTG")
            File "C:\Users\sleman\Testowanie automatyczne\laboratorium-7-tusiaa\Zad7-1.py", line 41, in distance
                raise ValueError('Wrong value.')
        ValueError: Wrong value.
        >>> h.distance("","G")
        Traceback (most recent call last):
            File "C:\Python310\lib\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.hamming.distance[7]>", line 1, in <module>
                h.distance("","G")
            File "C:\Users\sleman\Testowanie automatyczne\laboratorium-7-tusiaa\Zad7-1.py", line 41, in distance
                raise ValueError('Wrong value.')
        ValueError: Wrong value.
        >>> h.distance("G","")
        Traceback (most recent call last):
            File "C:\Python310\lib\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.hamming.distance[7]>", line 1, in <module>
                h.distance("G","")
            File "C:\Users\sleman\Testowanie automatyczne\laboratorium-7-tusiaa\Zad7-1.py", line 41, in distance
                raise ValueError('Wrong value.')
        ValueError: Wrong value.
        >>> h.distance("G",1)
        Traceback (most recent call last):
            File "C:\Python310\lib\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.hamming.distance[7]>", line 1, in <module>
                h.distance("G",1)
            File "C:\Users\sleman\Testowanie automatyczne\laboratorium-7-tusiaa\Zad7-1.py", line 41, in distance
                raise ValueError('Wrong type.')
        ValueError: Wrong type.
        >>> h.distance("G",None)
        Traceback (most recent call last):
            File "C:\Python310\lib\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.hamming.distance[7]>", line 1, in <module>
                h.distance("G",None)
            File "C:\Users\sleman\Testowanie automatyczne\laboratorium-7-tusiaa\Zad7-1.py", line 41, in distance
                raise ValueError('Wrong type.')
        ValueError: Wrong type.
        >>> h.distance("G",2.5)
        Traceback (most recent call last):
            File "C:\Python310\lib\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.hamming.distance[7]>", line 1, in <module>
                h.distance("G",2.5)
            File "C:\Users\sleman\Testowanie automatyczne\laboratorium-7-tusiaa\Zad7-1.py", line 41, in distance
                raise ValueError('Wrong type.')
        ValueError: Wrong type.
        >>> h.distance("G",True)
        Traceback (most recent call last):
            File "C:\Python310\lib\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.hamming.distance[7]>", line 1, in <module>
                h.distance("G",True)
            File "C:\Users\sleman\Testowanie automatyczne\laboratorium-7-tusiaa\Zad7-1.py", line 41, in distance
                raise ValueError('Wrong type.')
        ValueError: Wrong type.
        >>> h.distance("G",[1,2,3])
        Traceback (most recent call last):
            File "C:\Python310\lib\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.hamming.distance[7]>", line 1, in <module>
                h.distance("G",[1,2,3])
            File "C:\Users\sleman\Testowanie automatyczne\laboratorium-7-tusiaa\Zad7-1.py", line 41, in distance
                raise ValueError('Wrong type.')
        ValueError: Wrong type.
        """

        if type(a) != str or type(b) != str:
            raise ValueError('Wrong type.')
        if len(a) != len(b):
            raise ValueError('Wrong value.')    
        d = 0
        for i in range(0, len(a)):
            if b[i] != a[i]:
                d += 1
        return d
   

if __name__ == '__main__':
    import doctest
    doctest.testmod()
  