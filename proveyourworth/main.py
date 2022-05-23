import Modules as md
url = 'https://www.proveyourworth.net/level3/start'
username = 'Sebastian Yusti'
email = 'SebastianYusti21@protonmail.com'
data = {'X-Post-Back-Fields': 'image=,code=,resume=', 
        'X-Please-Also-Provide': f'email={email},name={username}', 
        'X-By-The-Way': "I consider myself a dedicated, sincere, creative and eager to learn person, I loved this challenge that was proposed to me!", 
        }
text = [f'Nombre: {username}', f'Hash:{list(md.get_params(url, username).values())[0]}', f'Email: {email}', 'Python Developer']
md.load_page(url,data=data, username=username)
md.write_img('bmw_for_life.jpg', text)