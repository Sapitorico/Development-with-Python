from sklearn.linear_model import LinearRegression
""" importa el modulo con un paquete """

X = [[1, 1], [2, 2], [3, 3], [4, 4]]
y = [2, 4, 6, 8]
modelo = LinearRegression()
modelo.fit(X, y)