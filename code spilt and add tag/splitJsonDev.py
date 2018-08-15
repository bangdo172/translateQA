import json
import os

with open("dev-v2.0.json", 'r') as file:
    data = json.load(file)['data']
    
article_count = 0
for article in data:
    title = article['title']
    article_folder = "article_" + str(article_count)
    os.makedirs(article_folder)
    article_count += 1
    paragraphs = article['paragraphs']
    paragraph_count = 0
    for paragraph in paragraphs:
        paragraph_file = 'paragraph_' + str(paragraph_count) + ".json"
        paragraph_count += 1
        with open(article_folder + "/" + paragraph_file, 'w') as file:
            json.dump(paragraph, file)