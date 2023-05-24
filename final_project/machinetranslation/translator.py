"""
This module translates from english to french and viceversa
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

# Set initial variables
api_key=os.environ['apikey']
api_url=os.environ['url']

# Prepare the authenticator
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(api_url)

# Translate from English to French
def english_to_french(english_text):
    """Get access to translator e returns translation json"""
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    mydict = translation['translations'][0]
    french_text = mydict['translation']
    return french_text

# Translate from French to English
def french_to_english(french_text):
    """Get access to translator e returns translation json"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    mydict = translation['translations'][0]
    english_text = mydict['translation']
    return english_text
