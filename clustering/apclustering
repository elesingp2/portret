from sklearn.manifold import LocallyLinearEmbedding
from sklearn.cluster import AffinityPropagation
import numpy as np

lle = LocallyLinearEmbedding(n_neighbors=10, n_components=2, method='standard')
ap = AffinityPropagation(damping=0.5,affinity="precomputed")

class ApClustering:
    def __init__(self, myu = 0.5, sigma = 0.8, a = 1):
        self.lle = lle
        self.ap = ap
        self.kernal = lambda xi, xj: myu / (1 + np.exp(-np.linalg.norm(xi - xj)**2 / a**2)) + (1 - myu) * np.exp(-np.linalg.norm(xi - xj)**2 / (2 * sigma**2))

    def Simular(self, X):
        Sim = np.zeros((len(X), len(X)))
        for i in range(len(X)):
            for j in range(len(X)):
                Sim[i, j] = self.kernal(X[i], X[j])
        return Sim

    def fit(self, X):
        X_transformed = self.lle.fit_transform(X)
        Sim_precomputed=self.Simular(X_transformed)
        labels=self.ap.fit_predict(Sim_precomputed)
        with open('labels.txt', 'w') as f:
            for label in labels:
                f.write("%s\n" % label)
        return labels