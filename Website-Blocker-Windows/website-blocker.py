host = "C:\Windows\System32\drivers\etc\hosts"
localhost = '127.0.0.1'
website_list = ["pornhub.com", "xnxx.com", "xvideos.com", "bangbros.com", "xxx.com",  "qualityporn.com",  "porn.com"]

while True:    
    with open(host, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(localhost + " " + website + "\n")
    break
