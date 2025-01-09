from flask import Flask, render_template, jsonify, send_file, after_this_request
import pypandoc
import os
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-docx', methods=['GET'])
def create_docx():
    try:
        # Χρησιμοποιήστε την πλήρη διαδρομή του αρχείου
        file_path = os.path.join(os.path.dirname(__file__), 'templates', 'Stylish teaching resume.html')
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Δημιουργήστε ένα προσωρινό αρχείο για την αποθήκευση του DOCX
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_file:
            tmp_file_path = tmp_file.name

        # Μετατροπή του HTML σε DOCX
        pypandoc.convert_text(html_content, 'docx', format='html', outputfile=tmp_file_path)

        @after_this_request
        def remove_file(response):
            try:
                os.remove(tmp_file_path)
            except Exception as e:
                app.logger.error(f"Error deleting temp file: {e}")
            return response

        # Στείλτε το αρχείο DOCX στον πελάτη
        return send_file(tmp_file_path, as_attachment=True, download_name='Stylish_teaching_resume.docx', mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    except Exception as e:
        app.logger.error(f"Error creating DOCX: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)