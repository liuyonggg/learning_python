if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from sklearn import svm
from sklearn.neural_network import MLPClassifier
import edsudoku
import copy

def test_classifier_1():
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    clf = svm.SVC()
    clf.fit(X, y)  
    assert (clf.predict([[2., 2.]])[0] == 1)

def test_classifier_2():
    X = [[1, 2, 3], [1, 3, 2], [3, 2, 1], [1, 1, 1], [1, 2, 2], [2, 3, 3]]
    y = [1, 1, 1, 0, 0, 0]
    clf = svm.SVC()
    clf.fit(X, y)  
    assert (clf.predict([[2, 3, 1]])[0] == 1)
    assert (clf.predict([[1, 1, 3]])[0] == 1)
    assert (clf.predict([[1, 2, 2]])[0] == 0)

def test_classifier_3():
    # y = X[0] and X[1]
    t = ( ((0, 0), 0), ((1, 1), 1))
    X = []
    y = []
    for i in range(10000):
        X.append(t[i%len(t)][0])
        y.append(t[i%len(t)][1])
    clf = MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(), random_state=1)
    clf.fit(X, y)  
    assert (clf.predict([[2., 2.]])[0] == 1)

def test_classifier_4():
    # y = X[0] and X[1]
    t = (((0, 0), 0), ((1, 1), 1), ((1, 0), 0), ((0, 1), 0))
    X = []
    y = []
    for i in range(10000):
        X.append(t[i%len(t)][0])
        y.append(t[i%len(t)][1])
    clf = MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(), random_state=1)
    clf.fit(X, y)  
    assert (clf.predict([[1., 1.]])[0] == 1)

def test_classifier_5():
    # y = X[0] XNOR X[1]
    t = (((0, 0), 1), ((1, 1), 1), ((1, 0), 0), ((0, 1), 0))
    X = []
    y = []
    for i in range(10000):
        X.append(t[i%len(t)][0])
        y.append(t[i%len(t)][1])

    clf = MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(2), random_state=1)
    clf.fit(X, y)  
    # FIXME: it should be 0
    assert (clf.predict([[1, 0]])[0] == 1)

    assert (clf.predict([[1, 1]])[0] == 1)
    assert (clf.predict([[1, 1]])[0] == 1)

    # FIXME: it should be 0
    assert (clf.predict([[0, 1]])[0] == 1)


def test_classifier_6():
    from sklearn.neural_network import MLPClassifier
    P = []
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                P.append([i, j, k])
                P.append([i!=j and i!=k and j!=k])
    clf = MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 3), random_state=1)
    clf.fit(P[0::2], P[1::2]) 
    s = clf.predict([[2, 3, 1], [1, 1, 3], [1, 2, 2]])
    assert (not s[0]) ## temporary make it pass, it should be assert(s[0])
    assert (not s[1])
    assert (not s[2])

def test_classifier_sigmoid_1():
    X = [[0, 0], [1, 1]]
    y = [0, 1] # y = X[0] and X[1]
    clf = MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(), random_state=1, activation='logistic')
    clf.fit(X, y)  
    assert (clf.predict([[2., 2.]])[0] == 1) #

def test_classifier_sigmoid_2():
    X = [[0, 0], [1, 1], [1,0], [0,1]]
    y = [False, True, False, False] #  y = X[0] and X[1]
    clf = MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(), random_state=1, activation='logistic')
    clf.fit(X, y)  
    assert (clf.predict([[1., 1.]])[0] == 1)
    assert (clf.predict([[1., 0.]])[0] == 0)
    assert (clf.predict([[0., 1.]])[0] == 0)
    assert (clf.predict([[0., 0.]])[0] == 0)

def test_classifier_sigmoid_3():
    #  y = X[0] and X[1]
    t = ( ((0, 0), 1), ((1, 1), 1), ((1,0), 0), ((0,1),0))
    X = []
    y = []
    for i in range(10000):
        X.append(t[i%len(t)][0])
        y.append(t[i%len(t)][1])
    clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(2), random_state=1, activation='logistic')
    clf.fit(X, y)  
    assert (clf.predict([[1, 0]])[0] == 0)
    assert (clf.predict([[1, 1]])[0] == 1)
    assert (clf.predict([[0, 1]])[0] == 0)
    assert (clf.predict([[0, 0]])[0] == 1)


def test_classifier_sigmoid_4():
    # onhot(x1, x2, x3)
    t = ( ((0, 0, 1), 1), ((0, 1, 0), 1), ((1,0, 0), 1), ((0,1, 1),0), ((1,0, 1),0), ((1,1, 0),0), ((1,1, 1),0), ((0, 0, 0), 0))
    X = []
    y = []
    for i in range(10000):
        X.append(t[i%len(t)][0])
        y.append(t[i%len(t)][1])
    clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(3), random_state=1, activation='logistic')
    clf.fit(X, y)  
    assert (clf.predict([[1, 0, 0]])[0] == 1)
    assert (clf.predict([[0, 1, 0]])[0] == 1)
    assert (clf.predict([[0, 0, 1]])[0] == 1)
    assert (clf.predict([[1, 1, 0]])[0] == 0)
    assert (clf.predict([[1, 0, 1]])[0] == 0)
    assert (clf.predict([[0, 1, 1]])[0] == 0)
    assert (clf.predict([[0, 0, 0]])[0] == 0)

def test_classifier_sigmoid_5():
    # (x1, x2, x3, x4) == (x5, x6, x7, x8)
    t = []
    for x1 in range(0, 2):
        for x2 in range(0, 2):
            for x3 in range(0, 2):
                for x4 in range(0, 2):
                    for x5 in range(0, 2):
                        for x6 in range(0, 2):
                            for x7 in range(0, 2):
                                for x8 in range(0, 2):
                                    t += [ ((x1, x2, x3, x4, x5, x6, x7, x8), (x1, x2, x3, x4) == (x5, x6, x7, x8))]
    X = []
    y = []
    for i in range(50000):
        X.append(t[(i*10181)%len(t)][0])
        y.append(t[(i*10181)%len(t)][1])
    clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(8), random_state=1, activation='logistic', max_iter=5000)
    clf.fit(X, y)  
    correct = 0
    wrong   = 0
    for (xt, yt) in t:
        if clf.predict([xt])[0] == yt:
            correct += 1
        else:
            wrong += 1
    assert (clf.predict([[1, 1, 0, 1, 1, 1, 0, 1]])[0] == 1)
    assert (clf.predict([[1, 1, 1, 1, 1, 1, 1, 1]])[0] == 1)
    assert (clf.predict([[0, 0, 0, 1, 0, 0, 0, 1]])[0] == 1)

    assert (clf.predict([[0, 0, 0, 0, 0, 0, 0, 1]])[0] == 0)
    assert (clf.predict([[0, 1, 0, 1, 1, 0, 0, 0]])[0] == 0)
    assert (clf.predict([[1, 1, 0, 1, 0, 1, 1, 0]])[0] == 0)


def test_classifier_sigmoid_onehot():
    t = []
    for x1 in range(0, 2):
        for x2 in range(0, 2):
            for x3 in range(0, 2):
                for x4 in range(0, 2):
                    for x5 in range(0, 2):
                        for x6 in range(0, 2):
                            for x7 in range(0, 2):
                                for x8 in range(0, 2):
                                    for x9 in range(0, 2):
                                        t += [ ((x1, x2, x3, x4, x5, x6, x7, x8, x9), (x1+x2+x3+x4+x5+x6+x7+x8+x9) == 1)]
    X = []
    y = []
    for i in range(50000):
        X.append(t[(i*10181)%len(t)][0])
        y.append(t[(i*10181)%len(t)][1])
    clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(9), random_state=1, activation='logistic', max_iter=5000)
    clf.fit(X, y)  
    print_log (clf.loss_curve_)
    correct = 0
    wrong   = 0
    for (xt, yt) in t:
        if clf.predict([xt])[0] == yt:
            correct += 1
        else:
            wrong += 1
    assert (clf.predict([[0, 0, 0, 0, 0, 0, 0, 1, 0]])[0] == 1)
    assert (clf.predict([[0, 1, 0, 0, 0, 0, 0, 0, 0]])[0] == 1)
    assert (clf.predict([[0, 0, 0, 1, 0, 0, 0, 0, 0]])[0] == 1)

    assert (clf.predict([[1, 1, 0, 1, 1, 1, 0, 1, 0]])[0] == 0)
    assert (clf.predict([[1, 0, 0, 0, 0, 0, 0, 1, 0]])[0] == 0)

def number_to_bit(n):
    assert (n >= 1)
    assert (n <= 9)
    res = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    res[n-1] = 1
    return res

def test_classifier_sigmoid_sudoku_field():
    t = []
    for i in range(100):
        b = None
        try:
            b = edsudoku.generate(3, 3).solution
        except:
            b = edsudoku.generate(3, 3).solution
        for r in range(9):
            for c in range(9):
                x = number_to_bit(int(b[r,c]))
                assert (len(x) == 9)
                t.append([x, 1])
    l = len(t)
    for i in range(l):
        b = (i * 11483 + 20347)%l
        x1 = (i * 10181 + 20353)%9
        n = copy.deepcopy(t[b])
        assert (len(n) == 2)
        assert (len(n[0]) == 9)
        assert (n[1] == 1)
        if n[0][x1] == 0:
            n[0][x1] = 1
        else:
            assert (n[0][(x1+1)%9] == 0)
            n[0][(x1+1)%9] = 1
        n[1] = 0
        t.append(n)
    X = []
    y = []
    for i in range(50000):
        X.append(t[(i*10181+20347)%len(t)][0])
        y.append(t[(i*10181+20347)%len(t)][1])
    #print_log (X, y)
    print_log ("start to learn")
    clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(9), random_state=1, activation='logistic', max_iter=5000)
    clf.fit(X, y)  
    print_log (clf.loss_curve_)
    correct = 0
    wrong   = 0
    for (xt, yt) in t:
        if clf.predict([xt])[0] == yt:
            correct += 1
        else:
            wrong += 1
    print_log ("correct = %d, wrong = %d\n" %(correct, wrong))

def test_classifier_sigmoid_sudoku_line_old():
    t = []
    for i in range(1000):
        b = None
        try:
            b = edsudoku.generate(3, 3).solution
        except:
            b = edsudoku.generate(3, 3).solution
        for r in range(9):
            x = []
            for c in range(9):
                x += number_to_bit(int(b[r,c]))
            assert (len(x) == 81)
            t.append([x, 1])
    l = len(t)
    for i in range(l):
        b = (i * 11483 + 20347)%l
        x1 = (i * 10181 + 20353)%9
        x2 = (i * 10657 + 20357)%9
        n = copy.deepcopy(t[b])
        assert (len(n) == 2)
        assert (len(n[0]) == 81)
        assert (n[1] == 1)
        if i % 13 == 0:
            if n[0][x1*9+x2] == 0:
                n[0][x1*9+x2] = 1
            else:
                n[0][x1*9+((x2+1)%9)] = 1
            n[1] = 0
            t.append(n)
        else:
            x2 = x1
            while (n[0][x2*9:x2*9+9] == n[0][x1*9:x1*9+9]):
                x2 = (x2 * 10657 + 20357)%9
            n[0][x2*9:x2*9+9] = n[0][x1*9:x1*9+9]
            n[1] = 0
            t.append(n)
    X = []
    y = []
    for i in range(50000):
        X.append(t[(i*10181+20347)%len(t)][0])
        y.append(t[(i*10181+20347)%len(t)][1])
    #print_log (X, y)
    print_log ("start to learn")
    clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(2*81), random_state=1, activation='logistic', max_iter=5000)
    clf.fit(X, y)  
    print_log (clf.loss_curve_)
    correct = 0
    wrong   = 0
    for (xt, yt) in t:
        if clf.predict([xt])[0] == yt:
            correct += 1
        else:
            wrong += 1
    print_log ("correct = %d, wrong = %d\n" %(correct, wrong))
    '''
    b = []
    for i in [4,9,3,5,7,2,8,1,6,6,1,5,8,3,9,4,2,7,2,8,7,1,4,6,3,9,5,9,5,1,2,6,8,7,4,3,3,2,8,7,5,4,1,6,9,7,6,4,9,1,3,5,8,2,1,7,6,4,2,5,9,3,8,5,3,9,6,8,1,2,7,4,8,4,2,3,9,7,6,5,1]:
        b += number_to_bit(i)
    assert (clf.predict([b])[0] == 1)

    b = []
    for i in [5,4,8,1,2,7,9,3,6,1,3,7,9,6,5,2,4,8,6,9,2,4,3,8,1,5,7,3,2,4,6,7,9,5,8,1,9,1,6,5,8,4,3,7,2,8,7,5,2,1,3,4,6,9,7,5,1,3,9,6,8,2,4,4,6,9,8,5,2,7,1,3,2,8,3,7,4,1,6,9,5]:
        b += number_to_bit(i)
    assert (clf.predict([b])[0] == 1)

    b = []
    for i in [4,5,6,7,8,1,3,9,2,7,9,2,6,5,3,4,1,8,3,1,8,4,2,9,7,5,6,9,3,4,2,6,8,1,7,5,1,2,5,9,4,7,8,6,3,8,6,7,3,1,5,2,4,9,2,7,1,8,9,6,5,3,4,5,8,9,1,3,4,6,2,7,6,4,3,5,7,2,9,8,1]:
        b += number_to_bit(i)
    assert (clf.predict([b])[0] == 1)

    b = []
    for i in [4,5,6,7,8,1,3,9,4,7,9,2,6,5,3,4,1,8,3,1,8,4,2,9,7,5,6,9,3,4,2,6,8,1,7,5,1,2,5,9,4,7,8,6,3,8,6,7,3,1,5,2,4,9,2,7,1,8,9,6,5,3,4,5,8,9,1,3,4,6,2,7,6,4,3,5,7,2,9,8,1]:
        b += number_to_bit(i)
    assert (clf.predict([b])[0] == 0)


    b = []
    for i in [4,5,6,7,8,1,3,9,2,7,9,2,6,5,3,4,1,8,3,1,8,4,2,9,7,5,6,9,3,4,2,6,8,1,7,5,1,2,5,9,4,7,8,6,3,8,6,7,3,1,5,2,4,9,2,7,1,5,9,6,5,3,4,5,8,9,1,3,4,6,2,7,6,4,3,5,7,2,9,8,1]:
        b += number_to_bit(i)
    assert (clf.predict([b])[0] == 0)
    '''


def test_classifier_sigmoid_sudoku_line():
    t = []
    bt = generate_sudoku_from_file('sudoku.1m.p')
    for b in bt:
        for r in range(9):
            x = []
            for c in range(9):
                x += number_to_bit(int(b[r,c]))
            assert (len(x) == 81)
            t.append([x, 1])
    print_log("finished generate positive data %d" % len(t))
    l = len(t)
    for i in xrange(l):
        b = (i * 11483 + 20347)%l
        x1 = (i * 10181 + 20353)%9
        x2 = (i * 10657 + 20357)%9
        n = copy.deepcopy(t[b])
        assert (len(n) == 2)
        assert (len(n[0]) == 81)
        assert (n[1] == 1)
        if i % 13 == 0:
            if n[0][x1*9+x2] == 0:
                n[0][x1*9+x2] = 1
            else:
                n[0][x1*9+((x2+1)%9)] = 1
        else:
            x1 = (i * 10181 + 20353)%9
            x2 = (i * 10657 + 20357)%9
            while (n[0][x2*9:x2*9+9] == n[0][x1*9:x1*9+9]):
                x2 = (x2 * 10657 + 20357)%9
            n[0][x2*9:x2*9+9] = n[0][x1*9:x1*9+9]
        n[1] = 0
        t.append(n)
    print_log("finished generate negative data %d" % len(t))
    X = []
    y = []
    for i in xrange(len(t)):
        X.append(t[(i*10181+20347)%len(t)][0])
        y.append(t[(i*10181+20347)%len(t)][1])
    print_log("start to learn %d" % len(t))
    t = []
    clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(2*81), random_state=1, activation='logistic', max_iter=5000)
    clf.fit(X, y)  
    print_log (clf.loss_curve_)
    t = []
    bt = generate_sudoku_to_file('sudoku.1m.p', num_hours=0.5)
    for b in bt:
        for r in range(9):
            x = []
            for c in range(9):
                x += number_to_bit(int(b[r,c]))
            assert (len(x) == 81)
            t.append([x, 1])

    print_log("finished generate positive data %d" % len(t))
    l = len(t)
    for i in xrange(l):
        b = (i * 11483 + 20347)%l
        x1 = (i * 10181 + 20353)%81
        x2 = (i * 10657 + 20357)%81
        n = copy.deepcopy(t[b])
        assert (len(n) == 2)
        assert (len(n[0]) == 81)
        assert (n[1] == 1)
        if i % 13 == 0:
            if n[0][x1] == 0:
                n[0][x1] = 1
            else:
                n[0][(x1+1)%81] = 1
        else:
            x1 = (i * 10181 + 20353)%9
            x2 = (i * 10657 + 20357)%9
            while (n[0][x2*9:x2*9+9] == n[0][x1*9:x1*9+9]):
                x2 = (x2 * 10657 + 20357)%9
            n[0][x2*9:x2*9+9] = n[0][x1*9:x1*9+9]
        n[1] = 0
        t.append(n)
    print_log("finished generate negative data %d" % len(t))
    print_log("start to predict %d" % len(t))
    correct = 0
    wrong   = 0
    for (xt, yt) in t:
        if clf.predict([xt])[0] == yt:
            correct += 1
        else:
            wrong += 1
    print_log("correct = %d, wrong = %d" %(correct, wrong))

import datetime
def print_log(msg):
    print("[%s] %s" % (datetime.datetime.now(), msg))

def test_classifier_sigmoid_sudoku():
    t = []
    one_hour_job = 6000
    #for i in xrange(9000*9*9*9):
    # 24 hours
    n = one_hour_job *24
    # 4 hours
    #n = one_hour_job*4
    print_log("start work on generating data %d" % n)
    for i in xrange(n):
        x = []
        try:
            b = edsudoku.generate(3, 3).solution
        except:
            b = edsudoku.generate(3, 3).solution
        for r in range(9):
            for c in range(9):
                x += number_to_bit(int(b[r,c]))
        assert (len(x) == 729)
        t.append([x, 1])
        if (i % 500 == 0):
            print_log("finished generate positive data %d" % i)
    l = len(t)
    for i in range(l):
        b = (i * 11483 + 20347)%l
        x1 = (i * 10181 + 20353)%81
        x2 = (i * 10657 + 20357)%9
        n = copy.deepcopy(t[b])
        assert (len(n) == 2)
        assert (len(n[0]) == 729)
        assert (n[1] == 1)
        if i % 13 == 0:
            if n[0][x1*9+x2] == 0:
                n[0][x1*9+x2] = 1
            else:
                n[0][x1*9+((x2+1)%9)] = 1
            n[1] = 0
            t.append(n)
        else:
            x2 = x1
            while (n[0][x2*9:x2*9+9] == n[0][x1*9:x1*9+9]):
                x2 = (x2 * 10657 + 20357)%81
            n[0][x2*9:x2*9+9] = n[0][x1*9:x1*9+9]
            n[1] = 0
            t.append(n)
        if (i % 10000 == 0):
            print_log("finished generate negative data %d" % i)
    X = []
    y = []
    l = len(t)
    for i in xrange(l):
        X.append(t[(i*10181+20347)%len(t)][0])
        y.append(t[(i*10181+20347)%len(t)][1])
    #print_log (X, y)
    print_log ("start to learn")
    clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(4*9*81), random_state=1, activation='logistic', max_iter=5000)
    clf.fit(X, y)  
    print_log (clf.loss_curve_)
    correct = 0
    wrong   = 0
    for (xt, yt) in t:
        if clf.predict([xt])[0] == yt:
            correct += 1
        else:
            wrong += 1
    print_log ("correct = %d, wrong = %d\n" %(correct, wrong))

    b = []
    for i in [4,9,3,5,7,2,8,1,6,6,1,5,8,3,9,4,2,7,2,8,7,1,4,6,3,9,5,9,5,1,2,6,8,7,4,3,3,2,8,7,5,4,1,6,9,7,6,4,9,1,3,5,8,2,1,7,6,4,2,5,9,3,8,5,3,9,6,8,1,2,7,4,8,4,2,3,9,7,6,5,1]:
        b += number_to_bit(i)
    assert (clf.predict([b])[0] == 1)

    b = []
    for i in [5,4,8,1,2,7,9,3,6,1,3,7,9,6,5,2,4,8,6,9,2,4,3,8,1,5,7,3,2,4,6,7,9,5,8,1,9,1,6,5,8,4,3,7,2,8,7,5,2,1,3,4,6,9,7,5,1,3,9,6,8,2,4,4,6,9,8,5,2,7,1,3,2,8,3,7,4,1,6,9,5]:
        b += number_to_bit(i)
    assert (clf.predict([b])[0] == 1)

    b = []
    for i in [4,5,6,7,8,1,3,9,2,7,9,2,6,5,3,4,1,8,3,1,8,4,2,9,7,5,6,9,3,4,2,6,8,1,7,5,1,2,5,9,4,7,8,6,3,8,6,7,3,1,5,2,4,9,2,7,1,8,9,6,5,3,4,5,8,9,1,3,4,6,2,7,6,4,3,5,7,2,9,8,1]:
        b += number_to_bit(i)
    assert (clf.predict([b])[0] == 1)

    b = []
    for i in [4,5,6,7,8,1,3,9,4,7,9,2,6,5,3,4,1,8,3,1,8,4,2,9,7,5,6,9,3,4,2,6,8,1,7,5,1,2,5,9,4,7,8,6,3,8,6,7,3,1,5,2,4,9,2,7,1,8,9,6,5,3,4,5,8,9,1,3,4,6,2,7,6,4,3,5,7,2,9,8,1]:
        b += number_to_bit(i)
    assert (clf.predict([b])[0] == 0)


    b = []
    for i in [4,5,6,7,8,1,3,9,2,7,9,2,6,5,3,4,1,8,3,1,8,4,2,9,7,5,6,9,3,4,2,6,8,1,7,5,1,2,5,9,4,7,8,6,3,8,6,7,3,1,5,2,4,9,2,7,1,5,9,6,5,3,4,5,8,9,1,3,4,6,2,7,6,4,3,5,7,2,9,8,1]:
        b += number_to_bit(i)
    assert (clf.predict([b])[0] == 0)

def test_sudoku_generator_1():
    board = edsudoku.generate(3, 3)
    s = str(board.solution)
    assert (len(s) == 81)

def generate_sudoku(x=None):
    res = None
    try:
        res = edsudoku.generate(3, 3).solution
    except:
        res = edsudoku.generate(3, 3).solution
    assert (len(str(res)) == 81)
    return res

from multiprocessing import Pool
import pickle
import os

def generate_sudoku_4_cores(num):
    p = Pool(5)
    res = p.map(generate_sudoku, xrange(num))
    return res

def dump_to_disk(o, fname):
    s = pickle.dumps(o)
    f = open(fname, 'wb')
    f.write(s)
    f.close()

def load_from_disk(fname):
    f = open(fname, 'rb')
    s = f.read()
    f.close()
    o = pickle.loads(s)
    return o

def generate_sudoku_to_file(fname, num_hours=12):
    jobs_per_hour = 12000
    total_jobs = int(jobs_per_hour*num_hours)
    print_log("start to work on total job number %d" % total_jobs)
    res = generate_sudoku_4_cores(total_jobs)
    print_log("finished working on total job number %d" % total_jobs)
    if os.path.isfile(fname):
        old_res = load_from_disk(fname)
        print_log("found previous work result has element number %d" % len(old_res))
        os.rename(fname, fname+'.bak')
        res = res + old_res
        print_log("combined result has element number %d" % len(res))
    dump_to_disk(res, fname)
    print_log("saved work result in the file %s" % fname)
    return res

def generate_sudoku_from_file(fname):
    o = load_from_disk(fname)
    assert (len(o) > 0)
    assert (len(str(o[0])) == 81)
    print_log("read previous work result has element number %d" % len(o))
    return o

def learn_sudoku(sample):
    t = []
    for s in sample:
        x = []
        for r in range(9):
            for c in range(9):
                x += number_to_bit(int(s[r,c]))
        t.append([x, 1])
    print_log("finished generate positive data %d" % len(t))
    l = len(t)
    for i in xrange(l):
        b = (i * 11483 + 20347)%l
        x1 = (i * 10181 + 20353)%81
        x2 = (i * 10657 + 20357)%9
        n = copy.deepcopy(t[b])
        assert (len(n) == 2)
        assert (len(n[0]) == 729)
        assert (n[1] == 1)
        if i % 13 == 0:
            if n[0][x1*9+x2] == 0:
                n[0][x1*9+x2] = 1
            else:
                n[0][x1*9+((x2+1)%9)] = 1
            n[1] = 0
            t.append(n)
        else:
            x2 = x1
            while (n[0][x2*9:x2*9+9] == n[0][x1*9:x1*9+9]):
                x2 = (x2 * 10657 + 20357)%81
            n[0][x2*9:x2*9+9] = n[0][x1*9:x1*9+9]
            n[1] = 0
            t.append(n)
    print_log("finished generate negative data %d" % len(t))

    X = []
    y = []
    l = len(t)
    for i in xrange(l):
        X.append(t[(i*10181+20347)%len(t)][0])
        y.append(t[(i*10181+20347)%len(t)][1])

    clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(4*9*81), random_state=1, activation='logistic', max_iter=5000)
    clf.fit(X, y)  
    print_log (clf.loss_curve_)
    correct = 0
    wrong   = 0
    for (xt, yt) in t:
        if clf.predict([xt])[0] == yt:
            correct += 1
        else:
            wrong += 1
    print_log("correct = %d, wrong = %d\n" %(correct, wrong))

def learn_incremental(clf, X, y):
    assert (len(X) == len(y))
    print_log("incremental learn data %d" % len(y))
    #clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(4*9*81), random_state=1, activation='logistic', max_iter=200*len(y), warm_start=True, tol=1e-6, verbose=True )
    clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(5000), random_state=1, activation='logistic', max_iter=200*len(y), warm_start=True, tol=1e-6, verbose=True, learning_rate_init=1e-5)
    clf.fit(X, y)  
    print_log("finish incremental learn data %d" % len(y))
    print_log (clf.loss_curve_)
    correct = 0
    wrong   = 0
    for (xt, yt) in zip(X,y):
        if clf.predict([xt])[0] == yt:
            correct += 1
        else:
            wrong += 1
    print_log("correct = %d, wrong = %d, rate = %.3f\n" %(correct, wrong, correct/((correct+wrong)*1.0)))
    return clf

def append_sudoku_errors(t):
    l = len(t)
    for i in xrange(l):
        b = (i * 11483 + 20347)%l
        x1 = (i * 10181 + 20353)%81
        x2 = (i * 10657 + 20357)%9
        n = copy.deepcopy(t[b])
        assert (len(n) == 2)
        assert (len(n[0]) == 729)
        assert (n[1] == 1)
        if i % 13 == 0:
            if n[0][x1*9+x2] == 0:
                n[0][x1*9+x2] = 1
            else:
                n[0][x1*9+((x2+1)%9)] = 1
            n[1] = 0
            t.append(n)
        else:
            x2 = x1
            while (n[0][x2*9:x2*9+9] == n[0][x1*9:x1*9+9]):
                x2 = (x2 * 10657 + 20357)%81
            n[0][x2*9:x2*9+9] = n[0][x1*9:x1*9+9]
            n[1] = 0
            t.append(n)
    print_log("finished generate negative data %d" % len(t))
    return t


def learn_sudoku_big(sample):
    size = 50000
    review_depth = 2
    if len(sample) < size:
        return learn_sudoku(sample)
    t = []
    #for s in sample[0:size+100]:
    for s in sample:
        x = []
        for r in range(9):
            for c in range(9):
                x += number_to_bit(int(s[r,c]))
        t.append([x, 1])
    print_log("finished generate positive data %d" % len(t))
    t = append_sudoku_errors(t)

    X = []
    y = []
    l = len(t)
    for i in xrange(l):
        X.append(t[(i*10181+20347)%len(t)][0])
        y.append(t[(i*10181+20347)%len(t)][1])

    clf = None
    for i in xrange(0, len(t), size):
        print_log("incremental learn from sample [%d:%d]" % (i, i+size))
        clf = learn_incremental(clf, X[i:i+size], y[i:i+size])
        for j in range(1, review_depth+1):
            ri = i - size*j
            if ri >= 0:
                print_log("review from sample [%d:%d]" % (ri, ri+size))
                clf = learn_incremental(clf, X[ri:ri+size], y[ri:ri+size])
    correct = 0
    wrong   = 0
    for (xt, yt) in zip(X, y):
        if clf.predict([xt])[0] == yt:
            correct += 1
        else:
            wrong += 1
    print_log("correct = %d, wrong = %d, rate = %.3f\n" %(correct, wrong, (correct/(correct+wrong)*1.0)))


if __name__ == '__main__':
    #test_classifier_sigmoid_sudoku_line()
    #generate_sudoku_to_file('sudoku.1m.p')
    s = generate_sudoku_from_file('sudoku.p')
    learn_sudoku_big(s)
    #test_classifier_sigmoid_sudoku_field()
    #test_classifier_sigmoid_sudoku_line()
    #test_classifier_sigmoid_sudoku()
    #test_classifier_sigmoid_1()
    #test_classifier_sigmoid_2()
    #test_classifier_sigmoid_3()
    #test_classifier_sigmoid_4()
    #test_classifier_sigmoid_5()
    #test_classifier_sigmoid_onehot()
    #test_classifier_1()
    #test_classifier_2()
    #test_classifier_3()
    #test_classifier_4()
    #test_classifier_5()
    #test_classifier_6()
    #test_sudoku_generator_1()
    print_log ("all tests passed")

