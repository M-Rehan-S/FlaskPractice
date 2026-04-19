from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Stacked routes are perfectly fine!
@app.route('/<name>', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index(name=None):
    app.secret_key = 'slfjklasdjklfjksaldjfkljdsklfjkl'
    if request.method == 'POST':
        # Safely grab the name from the submitted form using .get()
        form_name = request.form.get('name')
        return render_template('result.html', name=form_name) 
    else:
        # GET Request: Pass the URL 'name' variable into your index.html template!
        # If they visited '/', name will be None. If they visited '/Alice', name will be 'Alice'.
        return render_template('index.html', name=name)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('the_file')
        if file:
            file.save(f"files/{secure_filename(file.filename)}")
            flash('File uploaded successfully!', 'success')
        else:
            flash('No file selected.', 'error')
    return render_template('filetest.html')

if __name__ == '__main__':
    app.run(debug=True)