import urllib.request
import urllib.parse
import sys
 
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.txtlocal.com/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

apiKey = 'NSiOFMju1Aw-xRb9q5mwLvljHHTvXUwmiFcYvQKnXl'
mobileNumbers = ['+639356400087']
message = 'Hello, World!'
sender = 'fruitcrops07'

def populateMobileNumberToSingleString(mobileNumbers):
    numberListInSingelString = ''
    for number in mobileNumbers:
        numberListInSingelString += number + ','
    return numberListInSingelString.rstrip(',')

def validateCLIArguments():
    
    # we will start with index 1 because the default argument of python CLI is the source file itself
    index = 1
    while index < len(sys.argv):
        if(len(sys.argv[index]) != 13):
            raise Exception('Invalid Phone format. Valid format is : +63XXXXXXXXXX')
        index += 1
    print(sys.argv)

#resp =  sendSMS(apiKey, mobileNumbers[0], sender, message)
#print (resp)
validateCLIArguments()
print(populateMobileNumberToSingleString(sys.argv))