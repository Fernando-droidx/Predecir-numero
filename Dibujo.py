import tkinter as tk
from tkinter import messagebox
from PIL import ImageGrab, Image
import numpy as np
import tensorflow as tf

# Cargar el modelo entrenado
model = tf.keras.models.load_model('mi_modelo_mnist.h5')  # Carga tu modelo entrenado

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivinar el numero")
        self.canvas = tk.Canvas(self.root, bg="white", width=400, height=400)
        self.canvas.pack()

        self.old_x = None
        self.old_y = None

        self.canvas.bind('<B1-Motion>', self.draw)  # Botón izquierdo del mouse en movimiento
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        self.button_predict = tk.Button(self.root, text="Predecir", command=self.predict_digit)
        self.button_predict.pack()

    def draw(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=10, fill='black', capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def predict_digit(self):
        # Capturar el canvas y convertirlo a una imagen PIL
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()

        # Guardar la imagen del canvas
        image = ImageGrab.grab().crop((x, y, x1, y1)).convert("L")
        image = image.resize((28, 28))
        image = np.array(image)
        image = image / 255.0

        image = 1-image


        image = image.reshape(1, 28, 28, 1)

        # Predecir el dígito usando el modelo cargado
        prediction = model.predict([image])
        digit = np.argmax(prediction)

        # Mostrar la predicción
        print(f"Dígito predicho: {digit}")
        tk.messagebox.showinfo("Predicción", f"Dígito predicho: {digit}")

root = tk.Tk()
app = DrawingApp(root)
root.mainloop()
