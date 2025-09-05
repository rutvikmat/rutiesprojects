from flask import Flask, render_template, request, send_file
import markdown
import pdfkit
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        markdown_text = request.form['markdown_text']

        # Convert Markdown to HTML
        html_text = markdown.markdown(markdown_text)

        # Define output PDF path
        output_path = 'output.pdf'

        try:
            # Convert HTML to PDF
            pdfkit.from_string(html_text, output_path)

            # Send the file for download
            return send_file(output_path, as_attachment=True, download_name='converted.pdf')
        except Exception as e:
            # Handle case where wkhtmltopdf is not found
            return f"Error: {e}. Ensure wkhtmltopdf is installed and in your system's PATH."
        finally:
            # Clean up the generated PDF file
            if os.path.exists(output_path):
                os.remove(output_path)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)