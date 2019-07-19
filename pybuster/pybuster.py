import requests

url="http://kevin.nebulacyber.com"

def main():
    x = 0
    connect(url)
    addExtensions(x)

def readwordlist(wordlist):
    testWords = ['orange','apple','pear']
    for i in testwords:
        return 
    

def addExtensions(extensions):
    testextensions = ['php','html','asp']
    for i in testextensions:
        print(url + "/"+"index."+i)

def fireaway():
    print("fireaway")

def connect(url):
    client = requests.session()
    response = client.get(url)
    print(response)

main()
