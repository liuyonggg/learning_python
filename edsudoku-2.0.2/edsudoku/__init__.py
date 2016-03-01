if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    #sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from generator import generate
__author__ = 'Eli Daian <elidaian@gmail.com>'
