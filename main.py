import requests
from flask import Flask
from flask import render_template
from flask import request
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

subscription_key = "b8b0351c901a48798f744ee8713b2595"
assert subscription_key

app = Flask(__name__)

@app.route('/')
def hello_world():
  vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
  vision_analyze_url = vision_base_url + "analyze"

	# Set image_url to the URL of an image that you want to analyze.
  image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/" + \
	    "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"
  #if (request.form['submit_pic'] != 0) :
  #  image_url = request.form['submit_pic']
    
  headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
  params   = {'visualFeatures': 'Categories,Description,Color'}
  data     = {'url': image_url}
  response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
  response.raise_for_status()

  analysis = response.json()
  
  image_caption = analysis["description"]["captions"][0]["text"].capitalize()

  return image_url
  #return render_template('index.html', image_caption=image_caption)

if __name__ == '__main__':
  app.run()
