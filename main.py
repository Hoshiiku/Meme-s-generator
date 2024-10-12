# Importar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Resultados del formulario
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # obtener la imagen seleccionada
        selected_image = request.form.get('image-selector')

        # Asignación #2. Recepción del texto
        main_text = request.form.get("textTop")
        bottom_text = request.form.get("textBottom")

        # Assignment #3. Receiving the text's positioning
       
        color = request.form.get("color-selector")
        # Asignación #3. Recepción del posicionamiento del texto
        text_pos = request.form.get("textTop_Y")
        bottom_text_pos = request.form.get("textBottom_Y")

        

        return render_template('index.html', 
                               # Visualización de la imagen seleccionada
                               selected_image=selected_image, 

                               # Asignación #2. Visualización del texto
                               maintext = main_text,
                               bottom_text = bottom_text,

                               #  Asignación #3. Visualización del color
                               color = color,

                               
                               # Asignación #3. Visualización de la posición del texto
                               text_pos = text_pos,
                               bottom_text_pos = bottom_text_pos,


                               )
    else:
        # Mostrar la primera imagen por defecto
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
