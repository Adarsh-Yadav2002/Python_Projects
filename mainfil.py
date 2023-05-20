from flask import flask
from flask import request,render_template,url_for,send_file
import os,sys
import pdf3docx_import parse
 import typinfg-import Tuple
 from tkinter import T,messagebox
 from tkinter import_tkinter
 UPLOADER_FOLDER=''
 app=Flask(__name__)
 app.config['UPLOADER_FOLDER']=UPLOADER_FOLDER

  @ap.route('/')
  @app.route('/index'methods=['GET','POST'])
  def index():
    if request.method=="POST":
        def convert_pdf2docx(input_file:str,output_file;str,pages:Tuple=None):
          if pages:
              pages=[int(i) for i in list(pages) if i.isnumeric()]
            result=parse(pdf_ile=input_file,docx_wth_path=output_file, pages=pages)
        summar={"File": input_file,"pages":str(pages),"Output File":output_file}
        print("\n",join("{}:{}" .format(i,j) for i,j in summary.items()))
        return result
   files=request.files['filename']
   if file.filenamw!='':
    file.ave(os.path.join(app.config['UPLOADER_FOLDER'],file.filename))
    input_file=file.filename
    output_file=r"hello.docx"
    convert_pdf2docx(input_file,output_file)
    doc=input_file.split(".")[0]+"docx"
    lis=doc.replace(" ",'=')
    return render_template("docx.html",variable=lis)
render_template("index.html")

@app.route('/DOCX',methods=['GET','POST'])
def docx():
