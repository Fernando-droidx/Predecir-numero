import numpy as np
class Neurona:
    def __init__(self, n_pesos):
        self.W = np.random.rand(n_pesos)

    def _prop(self, X):
        return np.dot(self.W, X)
    def _act(self, z):
        return 1 / (1 + np.exp(-z))

    def forward(self, X):
        if len(X) != len(self.W):
            raise ValueError("El tamaño de la entrada no coincide con el número de pesos.")
        z = self._prop(X)
        
        output = self._act(z)

        return output


if __name__ == "__main__":
    neurona = Neurona(3)
    X = np.array([0.5, 0.2, 0.1])
    salida = neurona.forward(X)
    print("Salida de la neurona:", salida)
