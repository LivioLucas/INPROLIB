"""  <h1>Upload da Foto do Usuário</h1>
    <form id="uploadForm" enctype="multipart/form-data">
        <input type="file" name="photo" accept="image/*" required>
        <button type="submit">Enviar</button>
    </form>
    <img id="userPhoto" src="" alt="Foto do Usuário" style="display:none;"/>

*******************************************************************************

// script.js
document.getElementById('uploadForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const userPhoto = document.getElementById('userPhoto');
            userPhoto.src = data.photo_url; // URL da foto retornada
            userPhoto.style.display = 'block';
        } else {
            alert('Erro ao enviar a foto.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});


*******************************************************************************

from werkzeug.utils import secure_filename
import mysql.connector

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Pasta onde as fotos serão salvas
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Verifica se a extensão do arquivo é permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'photo' not in request.files:
        return jsonify(success=False)
    
    file = request.files['photo']
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Salvar o caminho da foto no banco de dados
        
        # Atualize o caminho da foto do usuário logado
        user_id = 1  # Suponha que você tenha a lógica para pegar o ID do usuário logado
        cursor.execute("UPDATE usuarios SET photo_path = %s WHERE id = %s", (filepath, user_id))
        connection.commit()
        cursor.close()
        connection.close()
        
        return jsonify(success=True, photo_url=filepath)
    
    return jsonify(success=False)


*******************************************************************************

  photo_path VARCHAR(255)  -- Coluna para armazenar o caminho da foto
  """