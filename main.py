import requests
from flask import Flask

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

  headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
  params   = {'visualFeatures': 'Categories,Description,Color'}
  data     = {'url': image_url}
  response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
  response.raise_for_status()

  analysis = response.json()
  print(analysis)

  image_caption = analysis["description"]["captions"][0]["text"].capitalize()

  return image_caption

if __name__ == '__main__':
  app.run()
