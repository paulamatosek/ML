from seaborn import load_dataset
from sklearn.datasets import load_iris

class MLWarmup:
    def getIrisDataset(self):
        iris = load_iris()
        index = 0
        while(index < len(iris['target'])):
            print(iris['data'][index], iris['target'][index], iris['target_names'][iris['target'][index]],
                  sep=' | ')
            index += 1
    def getPlanetsDataset(self):
        planets_df = load_dataset("planets")
        # print(planets_df)
        column_names = ['method', 'number', 'orbital_period', 'mass', 'distance', 'year']
        # ilość wartości pustych w kolumnach
        print(planets_df.isnull().sum())
        # usuń wszystkie kolumny zawierające więcej niż połowę wartości pustych - 1035
        half_dataset_no = int(len(planets_df)/2)
        planets_df1 = planets_df
        for c in column_names:
            if(planets_df[c].isnull().sum() > half_dataset_no):
                planets_df1 = planets_df1.drop(c,axis=1)
        print(planets_df1.isnull().sum())



ml = MLWarmup()
# ml.getIrisDataset()
ml.getPlanetsDataset()