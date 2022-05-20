from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
@app.route('/face_detection')
def face_detection():
   
   
   return render_template('fd.html',)   

@app.route('/social_distancing')
def social_distancing():
   return render_template('sdd.html')   

if __name__ == '__main__':
   app.run(debug=True)