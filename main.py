import tensorflow as tf
import tensorflow_datasets as tfds

(ds_train, ds_test), ds_info = tfds.load('mnist', split=['train', 'test'], as_supervised=True, with_info=True)

def preprocess_image(image, label):
    image = tf.cast(image, tf.float32) / 255.0  # Normalizar los píxeles entre 0 y 1
    return image, label

# Aplicar el preprocesamiento y agrupar los datos en lotes
ds_train = ds_train.map(preprocess_image).shuffle(1024).batch(32)
ds_test = ds_test.map(preprocess_image).batch(32)

# Crear red neuronal
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28, 1)),  # Convertir la imagen de 28x28 a un vector
    tf.keras.layers.Dense(128, activation='relu'),     # Capa oculta de 128 neuronas
    tf.keras.layers.Dense(10, activation='softmax')    # Capa de salida con 10 clases
])

# Compilar el modelo
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']  # precisión
)

# Entrenar el modelo
model.fit(ds_train, epochs=10)
print("modelo entrenado correctamente")

# Evaluar el modelo con el conjunto de prueba
test_loss, test_acc = model.evaluate(ds_test)
print(f"Precisión en el conjunto de prueba: {test_acc}")

# Guardar el modelo para uso futuro
model.save('mi_modelo_mnist.h5')
print("Modelo guardado como 'mi_modelo_mnist.h5'")
