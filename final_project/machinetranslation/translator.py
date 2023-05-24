import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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
def englishToFrench(englishText):
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    
    mydict = translation['translations'][0]
    frenchText = mydict['translation']
    return frenchText

# Translate from French to English
def frenchToEnglish(frenchText):
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    
    mydict = translation['translations'][0]
    englishText = mydict['translation']
    return englishText