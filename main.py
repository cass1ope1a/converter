from flask import Flask, render_template, request, send_file, make_response
from PyPDF2 import PdfReader
import tempfile

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert_pdf_to_text():
    if 'file' in request.files:
        pdf_file = request.files['file']
        reader = PdfReader(pdf_file)

        # Создаем временный файл
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt', encoding='utf-8') as temp_file:
            # Записываем содержимое PDF файла непосредственно в файл
            for page in reader.pages:
                temp_file.write(page.extract_text() + "\n")

        # Отправляем временный файл в качестве вложения
        return send_file(
            temp_file.name,
            as_attachment=True,
            mimetype='text/plain'
        )
    else:
        return 'No file provided'

@app.route('/metrics')
def metrics():
    response = make_response("hello world", 200)
    response.mimetype = "text/plain"
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
