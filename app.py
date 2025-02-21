from flask import Flask , render_template, request
from text_summary import summarizer

app = Flask(__name__)

@app.route("/" , methods = ['GET','POST'])
def index():
    summary = rawdocs = len_summary = len_rawdocs = None
    if request.method == 'POST':
        rawtext = request.form['text']
        summary ,rawdocs ,len_summary, len_rawdocs = summarizer(rawtext)
    
    return render_template("index.html",summary=summary,rawdocs=rawdocs,len_summary=len_summary,len_rawdocs=len_rawdocs)
if __name__ == "__main__":
    app.run(debug=True)
