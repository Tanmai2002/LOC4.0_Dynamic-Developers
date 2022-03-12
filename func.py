import requests

backRmapi='yMp43NNBqnCosi67pj5y87F5'
def removeBack(imgLoc,path):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(imgLoc, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': backRmapi},
    )
    if response.status_code == requests.codes.ok:
        with open(path, 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)