import requests

print("Welcome to the Website Status Checker!")
option = ''
while option != 'n':
    if option != 'n':
        urls = input("What URL you want to check? (Use commas to separate them): ").lower()
        urls_list = urls.split(',')
        
        
        for url in urls_list:
            try:
                if "." not in url:
                    print(f'Invalid URL: "{url}"')
                    break
                if "http" not in url:
                    url = "http://"+url.strip()
                       
                url_request = requests.get(url)
                if url_request.status_code == 200:
                    print(f"\n{url.strip()} website is online!")
                
            except requests.exceptions.RequestException:
                print(f"\n{url} website is offline")
        
    
    while option != 'n' or option != 'y':
        option = input("Do you wish to check another website? (y/n): ").lower()

        if option == 'n':
            print("Thank you, see you next time!")
            break
        elif option == 'y':
            break
        else:
            print("invalid option")
        
    