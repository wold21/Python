import urllib.request
import time
timenow = int(time.strftime('%d', time.localtime(time.time())))
i = 0
while(1):
    try:
        def GetPhoto(i):
            url = 'https://www.thispersondoesnotexist.com/image'
            user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36"
            request = urllib.request.Request(url, headers={'User-Agent': user_agent})
            response = urllib.request.urlopen(request)
            html = response.read()
            f = open('다운받을 경로를 넣어주시기 바랍니다.' + str(time.strftime('%Y%m%d', time.localtime(time.time()))) + '-' + str(i) + '.jpg', 'wb')
            f.write(html)
            f.close()
        GetPhoto(i)
        if(timenow < int(time.strftime('%d', time.localtime(time.time())))):
            timenow = int(time.strftime('%d', time.localtime(time.time())))
            i = 0
        else:
            i += 1
    except:
        print("Error Occurred at " + str(time.strftime('%m%d - %H:%M:%S', time.localtime(time.time()))))
        continue
