import urllib.request
for i in range(10000):
    def GetPhoto():
        url = 'https://www.thispersondoesnotexist.com/image'
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36"
        request = urllib.request.Request(url, headers={'User-Agent': user_agent})
        response = urllib.request.urlopen(request)
        html = response.read()
        f = open('./img/' + str(i) + '.jpg', 'wb')
        f.write(html)
        f.close()
    GetPhoto()
print("Finished")
