from sklearn import svm


X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]


lin_clf = svm.LinearSVC(verbose=True)
lin_clf.fit(X, Y)
dec = lin_clf.decision_function([[1]])
result = dec.shape[1]
print('result: ', result)
