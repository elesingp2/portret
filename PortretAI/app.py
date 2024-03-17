from flask import Flask, render_template
import sass

app = Flask(__name__)

# Функция для компиляции SCSS в CSS
def compile_scss():
    with open('/workspaces/portret/PortretAI/templates/styles.scss', 'r') as scss_file:
        scss_content = scss_file.read()
    return sass.compile(string=scss_content)

@app.route('/')
def home():
    # Компиляция SCSS в CSS и сохранение в статической директории
    compiled_css = compile_scss()
    with open('/workspaces/portret/PortretAI/static/styles.css', 'w') as css_file:
        css_file.write(compiled_css)
    # Рендеринг HTML с использованием скомпилированного CSS
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

