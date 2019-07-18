import requests

url="http://kevin.nebulacyber.com"

def main():
    connect(url)

def readwordlist(wordlist):
    testWords = ['orange','apple','pear']
    

def addExtensions(extensions):
    testextensions = ['php','html','asp']

def fireaway():
    print("fireaway")

def connect(url):
    client = requests.session()
    response = client.get(url)
    print(response.text)

main()
