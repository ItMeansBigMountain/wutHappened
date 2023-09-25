import os
import json

from NewsApi import NewsApi
from ImageGenerator import ImageGenerator
from ScriptGenerator import ScriptGenerator

# INIT MODEL STORAGE
cache_dir = os.path.abspath("./my_model_cache")
os.environ['TRANSFORMERS_CACHE'] = cache_dir

# INIT DATA INGESTION 
news = NewsApi(api=True, webscrape=False)

# INIT AI MODELS
image_gen = ImageGenerator("stabilityai/stable-diffusion-xl-base-1.0", cache_dir=cache_dir)
script_gen = ScriptGenerator("distilgpt2", device=0)

# INIT OUTPUT DIR
output_dir = os.path.abspath("./output/")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize dictionary to hold article data
article_data = {}

# Fetch news articles
articles = news.fetch_api()

# Generate images and scripts
for idx, article in enumerate(articles):
    # GENERATE IMAGE
    if article.get('description') is None:
        image = image_gen.generate_image(article.get('title'))
    else:
        image = image_gen.generate_image(article.get('description'))
    
    # GENERATE SCRIPT
    if article.get('description') is None:
        script = script_gen.generate_script(
            article.get('title'), max_length=100, num_return_sequences=1
        )
    else:
        script = script_gen.generate_script(
            article.get('description'), max_length=100, num_return_sequences=1
        )

    # Save Images and News Scripts
    image_path = os.path.join(output_dir, f"image_{idx}.png")
    image.save(image_path)
    
    # Populate dictionary with article data
    article_data[idx] = {
        "title": article.get('title'),
        "original_story": article.get('description'),
        "script": script,
        "image": image_path,
        "news_source": article.get('source'),
        "author": article.get('author'),
    }

    print(f"Saved image and script for article {idx} to {output_dir}")

# Save dictionary as JSON file
json_path = os.path.join(output_dir, "article_data.json")
with open(json_path, "w", encoding='utf-8') as f:
    json.dump(article_data, f, ensure_ascii=False, indent=4)