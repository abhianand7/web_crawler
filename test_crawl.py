import re, urllib3

textfile = file('/home/ubuntu/PycharmProjects/myproject/depth_1.txt','wt')
http = urllib3.PoolManager()
print "Enter the URL you wish to crawl.."
print 'Usage  - "http://phocks.org/stumble/creepy/" <-- With the double quotes'
myurl = input("@> ")
count = 0
for i in re.findall('''href=["']([^"']+)["']''', http.request('GET',myurl).data, re.I):
        print i
        count += 1
        for ee in re.findall('''href=["']([^"']+)["']''', http.request('GET',i).data, re.I):
                print ee
                count += 1
                textfile.write(ee+'\n')
textfile.close()
print('Total no of links found : %s' % count)
