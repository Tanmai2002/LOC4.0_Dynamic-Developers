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
def bw2color(imgLoc,path):
    import requests

    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={
            'image': open(imgLoc, 'rb'),
        },
        headers={'api-key': '9c6e52f2-eca9-4cce-85dd-5fa806dbe175'}
    )
    op=requests.get(r.json().get('output_url'))
    if op.status_code == 200:
        with open(path, 'wb') as f:
            f.write(op.content)