from sklearn.datasets import load_iris

class MLWarmup:
    def getIrisDataset(self):
        iris = load_iris()
        print(iris)

ml = MLWarmup()
ml.getIrisDataset()
