import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def translate(text, target):
    return language_translator.translate(
        text,
        model_id=target).get_result()


def englishToFrench(englishText):
    translation = translate(englishText, 'en-fr')
    frenchText = translation.get('translations')[0].get('translation')
    return frenchText


print(englishToFrench("Hello, how are you today?"))


def frenchToEnglish(frenchText):
    translation = translate(frenchText, 'fr-en')
    enText = translation.get('translations')[0].get('translation')
    return enText


print(frenchToEnglish("Ca va bien, merci"))
