# 🖌️✨ Dibujo y Reconocimiento de Dígitos con Redes Neuronales

Bienvenido a mi proyecto de **reconocimiento de dígitos escritos a mano** usando una red neuronal entrenada con el famoso dataset **MNIST**. En esta aplicación, los usuarios pueden dibujar números en un lienzo, y el modelo predice el dígito. 🎨🤖

## 🎯 Objetivos del Proyecto

Este proyecto combina **machine learning** y una interfaz de usuario interactiva con **Tkinter** para:
- Permitir al usuario **dibujar dígitos**.
- Utilizar un **modelo de red neuronal entrenado** para **predecir** el número dibujado.
- Crear una experiencia visual atractiva y fácil de usar. 

## 🛠️ Tecnologías Utilizadas

- **Python** 🐍
- **TensorFlow** para la creación y entrenamiento del modelo de red neuronal 🤖
- **Tkinter** para la interfaz gráfica de usuario 🎨
- **Pillow (PIL)** para la manipulación de imágenes 🖼️

## 📦 Estructura del Proyecto

##### RedNeuronalPrincipal ├── 📄 main.py  Código para entrenar y guardar el modelo ├── 📄 dibujo.py 📂
##### Aplicación gráfica con Tkinter para dibujar y predecir dígitos ├── 📄 mi_modelo_mnist.h5 
##### Modelo entrenado guardado ├── 📄 README.md 
##### Neurona, practica para hacer neuronas faciles 📄
##### Examples, mejora a primeros algoritmos 📄

## Instalación y Ejecución

### 1. Clonar el repositorio
git clonehttps://github.com/Fernando-droidx/Predecir-numero
cd RedNeuronalPrincipal` 

### 2. Instalar las dependencias

Asegúrate de tener **Python 3.7+** y ejecuta:

`pip install tensorflow pillow` 

### 3. Entrenar el modelo

Si deseas reentrenar el modelo o mejorarlo, ejecuta el archivo `main.py`:

`python main.py` 

Esto entrenará el modelo con el dataset **MNIST** y lo guardará como `mi_modelo_mnist.h5`.

### 4. Ejecutar la aplicación de dibujo

Para comenzar a dibujar y predecir dígitos, ejecuta:

`python dibujo.py` 

¡Ahora puedes dibujar números y ver cómo el modelo predice el dígito! 🎉

## 👩‍💻 Uso de la Aplicación

1.  Abre la aplicación.
2.  Dibuja un dígito usando tu mouse.
3.  Haz clic en el botón **Predecir**.
4.  Verás un cuadro emergente con el número que el modelo predijo. ¡Intenta dibujar diferentes números y comprueba la precisión! 🖊️🔢

## 📈 Mejoras Futuras

-   🏋️‍♂️ **Mejorar el modelo** con más datos y ajustar la arquitectura de la red neuronal.
-   🎨 **Agregar más opciones de dibujo**: cambiar el color, grosor del pincel, etc.
-   🌐 **Implementar una interfaz web** para acceder a la aplicación desde cualquier navegador.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el proyecto, siéntete libre de abrir un issue o enviar un pull request. 🙌

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Puedes ver más detalles en el archivo `LICENSE`. 📜

----------

### ✨ ¡Gracias por visitar este proyecto! Espero que te diviertas probándolo. 😊