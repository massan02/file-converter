import markdown
import sys

def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

        html = markdown.markdown(text)

    with open(output_file, 'w',encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Usage: python file-converter.py <input-file> <output-file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_markdown_to_html(input_file, output_file)