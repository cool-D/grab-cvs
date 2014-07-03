import re
import urllib2
from threading import Timer

record = open('test.html', 'w')
record.write('<html><body>')
for i in range(1,5):
    url="http://www.exploit-db.com/exploits/"+str(i)+"/"
    try:
        html = urllib2.urlopen(url).read()
        catt = re.compile(r'.*cve.mitre.org/cgi-bin/cvename.cgi\?name=(.*)\" target=.*')
        tablefind = catt.findall(html)	
        record.write(str(i)+'.'+'<a href="'+url+'" >'+tablefind[0]+'</a><br>')
        print "Num %d ok..." %i
        sleep(2)
    except:
        continue
record.write('</body></html>')
record.close()

print "Over, have fun~"
