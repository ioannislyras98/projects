import os
import docx
import pypandoc

def convert_docx_to_html(docx_path, html_path):
    # Set the PYPANDOC_PANDOC environment variable to the path of the pandoc executable
    os.environ["PYPANDOC_PANDOC"] = "C:/Program Files/Pandoc/pandoc.exe"
    
    # Convert the Word document to HTML using pypandoc
    output = pypandoc.convert_file(docx_path, 'html', extra_args=["--standalone"])
    
    # Write the HTML to a file
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(output)

if __name__ == "__main__":
    current_dir = os.getcwd()
    docx_path = os.path.join(current_dir, 'Stylish teaching resume.docx')
    html_path = os.path.join(current_dir, 'Stylish teaching resume.html')
    convert_docx_to_html(docx_path, html_path)
    print(f"Converted {docx_path} to {html_path}")