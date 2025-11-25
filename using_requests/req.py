# making requests to API end-points
# the requests library lets us make get, post etc requests to API end-points over http(s)
# NB you may need to pip install requests
import requests

# delcare a function for getting data
def getPhotos():
    '''retrieve all photo JSON data from remote API end-point'''
    url = 'https://jsonplaceholder.typicode.com/photos'
    try:
        response = requests.get(url) # the vast majority or requests will use 'get'
        # NB the response object will contain a lot of meta data, including status code, headers etc.
        photos = response.json() # this will extract the JSON data from the response object
        return photos
    except Exception as err:
        print(f'Something went wrong: {err}')

def checkInRange(v):
    '''validate v is a positive integer 1-5000'''
    if v in range(1,5001): # this is clever, it will only validate integer values
        return v # all good
    else:
        return 1 # just choose a sensible default

def getOnePhoto(n=1): 
    '''retrieve a single photo using the id value n
    Validate that n is a positive integer 1-5000'''
    n = checkInRange(n)
    url = 'https://jsonplaceholder.typicode.com/photos'
    try:
        response = requests.get(f'{url}/{n}')
        photo=response.json()
        return photo
    except Exception as err:
        print(f'Something went wrong: {err}')

# exercise the code
if __name__ == '__main__':
    '''this will only run when this module is directly invoked'''
    p = getPhotos()
    print(p)
    d = getOnePhoto(321)
    print(f"{d['title']} {d['thumbnailUrl']}")