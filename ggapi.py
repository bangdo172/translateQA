import argparse
import json
import os
from google.cloud import translate
import six

def translate_text_with_model(target, text, model=translate.NMT):
    # [START translate_text_with_model]
    """Translates text into the target language.
    Make sure your project is whitelisted.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target, model=model)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))
    # [END translate_text_with_model]


def translate_text(target, text):
    # [START translate_translate_text]
    """Translates text into the target language.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))
    # [END translate_translate_text]

if __name__ == '__main__':
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/bangdo/Documents/theProject/MachinelearningCode/ReadingWikiToAnswerOpenQuestion/translateAPI/DrQA-e18c69726d79.json'
	for eachFolder in os.listdir("/Users/bangdo/Documents/theProject/MachinelearningCode/ReadingWikiToAnswerOpenQuestion/translateAPI/dev"):
	    if (eachFolder != ".DS_Store"):
	        for eachFile in os.listdir("/Users/bangdo/Documents/theProject/MachinelearningCode/ReadingWikiToAnswerOpenQuestion/translateAPI/dev/" + eachFolder):
	            if (eachFile != ".DS_Store"):
	                with open("dev/" + eachFolder + "/" + eachFile, "r") as file:
	                    database = json.load(file)
	                print(type(database['context']))
	                translate_text('vi', database['context'])