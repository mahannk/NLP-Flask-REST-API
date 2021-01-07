# -*- coding: utf-8 -*-
from flask import Flask, g
from flask_restful import Resource, Api, reqparse
import numpy as np
import markdown
import ast
import spacy


app = Flask(__name__)
api = Api(app)

nlp = spacy.load("en_core_web_sm")


@app.route("/")
def index():
    return markdown.markdown("## Flask API is up and running")

class prediction(Resource):
    def post(self):
        """Process documents for part-of-speech tagging

        Returns:
            dict: a dictionary of predicted tags
        """         
        parser = reqparse.RequestParser()
        parser.add_argument('articles', type=str, action='append', required=True)
        args = parser.parse_args()
        
        results = [] 
        for article in args.articles:
            print(article)

            doc = nlp(article)
            for ent in doc.ents:
                results.append({"text" : ent.text, "label" : ent.label_})

            
        return {'message' : 'success', 'tags' : results}, 202

# request must be in format of: localhost:Port/query
api.add_resource(prediction, '/query')