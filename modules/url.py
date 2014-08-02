## SHUO MODULE ##
"""
URL Titles

Version: 1.0.0
Author: Emma Jones (AwwCookies)

Desc:
    Tells you the title of a URL said in a channel
"""
import re
import urllib2
from BeautifulSoup import BeautifulSoup
import pafy as youtube

class SH_MODULE(sh.Module):
    def __init__(self):
        sh.Module.__init__(self)

    def get_title(self, url):
        return BeautifulSoup(urllib2.urlopen(url)).title.string

    def cts(self, rating):
        'convert rating to stars'
        return '\x02\x0308\xe2\x98\x86' * int(round(float(rating))) # \xe2\x98\x86 is a white star

    def _youtube(self, url):
        video = youtube.new(url)
        send_message(data['Channel'], '\x0305You\x0314Tube\x03(http://youtu.be/%s): ' % video.videoid +\
        'Title: %s Views: %s Rating: %s' % (video.title, "{:,}".format(int(video.viewcount)), video.rating))

    def on_message(self, data):
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data['Message'])
        print urls
        for url in urls:
            if 'youtube.com' in url or 'youtu.be' in url:
                self._youtube(url)
            else:
                print url, self.get_title(url)
                send_message(data['Channel'], "[%s] => %s" % (url, str(self.get_title(url)).replace('\n', '').lstrip()))