import requests, os
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

def get_params(url,username)->dict:
    h = requests.get(url)
    soup = BeautifulSoup(h.content, 'html.parser')
    hashin = soup.select_one("input").attrs.get("value", None)
    return {'statefulhash':hashin, 'username':username}

def load_page(url,data,files,username='admin', getps='activate'):
    meta = get_params(url, username)
    with requests.session() as session:
        r = session.post(url, headers={'sec-fetch-site': 'same-origin'})
        r = session.get(f'https://www.proveyourworth.net/level3/{getps}', params=meta)
        url_payload = session.post(r.headers['X-Payload-URL'])
        if url_payload.status_code == 200:
            print(f'Correctly connected to {url_payload.url}')
        download_image(url_payload.content, file='bmw_for_life.jpg')
        cookies = {'x-oh-look':str(url_payload.headers['set-cookie']).strip('; path=/')}
        print(data)
        send = session.post(url_payload.headers['X-Post-Back-To'], data=data, files=files,cookies=cookies, verify=False)
        print(send.content)
        print(send.headers)
    
def download_image(content, file=''):
    try:
        with open(file, 'wb') as img:
            img.write(content)
            img.close()
        for file_ in os.listdir(os.getcwd()):
            if file_ == file: 
                x = True;
                break
            else: False
        print('Image downloaded correctly')
    except x==False:
        print('Image did not download...') 
        
def write_img(file, text, n=20):
    image = Image.open(file)
    dr = ImageDraw.Draw(image)
    for t in text:
        font = ImageFont.load_default()
        dr.text((40+10,10+n), t, fill=(61, 220, 35), font=font)
        n+=10
    image.save(file)
    
    
