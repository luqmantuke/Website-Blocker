# This is  a website blocker for linux
website_lists = ['pornhub.com', 'xnxx.com', 'xvideos', 'bangbros']
path = '/etc/hosts'
localhost = '127.0.0.1'

def main():
    while True:
        with open(path, '+r') as file:
            content = file.read()
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(localhost + ' ' + website + '\n' )
        break
            
if __name__ == "__main__":
    main()
