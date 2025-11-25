# making requests to API end-points
# the requests library lets us make get, post etc requests to API end-points over http(s)
# NB you may need to pip install requests
import requests

# delcare a function for getting data
def getPhotos():
    '''retrieve all photo JSON data from remote API end-point'''
    url = 'https://jsonplaceholder.typicode.com/photos'
    response = requests.get(url) # the vast majority or requests will use 'get'
    # NB the response object will contain a lot of meta data, including status code, headers etc.
    photos = response.json() # this will extract the JSON data from the response object
    return photos

# exercise the code
if __name__ == '__main__':
    '''this will only run when this module is directly invoked'''
    p = getPhotos()
    print(p)