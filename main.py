import requests
import os
from flask import Flask
from flask import render_template
from flask import request


subscription_key = "b8b0351c901a48798f744ee8713b2595"
assert subscription_key

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
x=""

@app.route('/')
def hello_world():
  #return image_caption
  return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
  file = request.files['image']

  f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
  file.save(f)
  
  vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
  vision_analyze_url = vision_base_url + "analyze"

  headers = {'Ocp-Apim-Subscription-Key': subscription_key }
  params = {'visualFeatures': 'Categories,Description,Color'}
  data = {'url': 'uploads/'+file.filename}
  response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
  response.raise_for_status()

  analysis = response.json()
  image_caption = analysis["description"]["captions"][0]["text"].capitalize()

  return render_template('index.html', image_caption=image_caption)
    
if __name__ == '__main__':
  app.run()
