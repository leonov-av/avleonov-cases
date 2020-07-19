import re
import os
import datetime
from mutagen.mp3 import MP3

############################ ITEM Description

title = "Barapass, Tsunami scanner, vulnerabilities in Windows DNS Server and SAP products, weird attack on Twitter"
blogpost_url = "https://avleonov.com/2020/07/18/barapass-tsunami-scanner-vulnerabilities-in-windows-dns-server-and-sap-products-weird-attack-on-twitter/"
youtube_url = "https://www.youtube.com/watch?v=nKul8wvdaTM"
description_html = r'''This episode is based on posts from <a href="https://t.me/avleonovcom">my Telegram channel avleonovcom</a>, published in the last 2 weeks. So, if you use Telegram, please subscribe. I update it frequently.'''
number = 11
file_path = r'''C:\Users\Alexander\Desktop\AVLEONOV Media\podcast\11-Barapass_Tsunami_scanner_vulnerabilities_in_Windows_DNS_Server_and_SAP_products_weird_attack_on_Twitter.mp3'''

############################

date_from_blogpost_url = blogpost_url.split("/")[3] + "." + blogpost_url.split("/")[4] + "." + blogpost_url.split("/")[5]
date_time_obj = datetime.datetime.strptime(date_from_blogpost_url, '%Y.%m.%d')
pubdate = date_time_obj.strftime('%a, %d %b %Y 12:00:00 GMT')
guid = date_time_obj.strftime('avleonov%d%b%Y')

#https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior   ->  Directive Meaning

filename = re.sub(",","",title)
filename = re.sub(":","",filename)
filename = re.sub(" ","_",filename)
filename += ".mp3"
filename = str(number) + "-" + filename

file_url = "http://avleonov.com/podcast/" + filename
# TO DO: get date and make
#      <guid>avleonov23Jun2020</guid>
#      <pubDate>Tue, 23 Jun 2020 12:00:00 GMT</pubDate>

template = '''
    <item>
      <itunes:episodeType>full</itunes:episodeType>
      <itunes:image href="https://avleonov.com/podcast/logo.png"/>
      <title>###TITLE###</title>
      <itunes:title>###TITLE###</itunes:title>
      <itunes:subtitle>###SUBTITLE###</itunes:subtitle>
      <content:encoded>
          <![CDATA[###DESCRIPTIONHTML###
          <br/>
          Watch the <a href="###YOUTUBEURL###">video version of this episode</a> on my YouTube channel.
          <br/>
          Read <a href="###BLOGPOSTURL###">the full text of this episode with all links</a> on avleonov.com blog.
          ]]>
      </content:encoded>
      <description>
          ###DESCRIPTIONTXT###
          Watch the video version of this episode on my YouTube channel.
          Read the full text of this episode with all links on avleonov.com blog.
      </description>
      <link>###BLOGURL###</link>
      <enclosure 
        length="###FILESIZE###"
        type="audio/mpeg" 
        url="###FILEURL###"
      />
      <guid>###GUID###</guid>
      <pubDate>###PUBDATE###</pubDate>
      <itunes:duration>###DURATION###</itunes:duration>
      <itunes:explicit>false</itunes:explicit>
    </item>
'''


if file_path != "":
    print(file_path)
    file_size = str(os.path.getsize(file_path))
    audio = MP3(file_path)
    audio_duration = str(int(audio.info.length))

    subtitle = re.sub("<[^>]*>","",description_html)
    subtitle = re.sub("\. .*",".",subtitle)

    description_txt = re.sub("<[^>]*>","",description_html)

    item = template
    item = re.sub("###TITLE###", "Ep." + str(number) + " - " + title, item)
    item = re.sub("###SUBTITLE###", subtitle, item)
    item = re.sub("###DESCRIPTIONHTML###", description_html, item)
    item = re.sub("###YOUTUBEURL###", youtube_url, item)
    item = re.sub("###BLOGPOSTURL###", blogpost_url, item)
    item = re.sub("###DESCRIPTIONTXT###", description_txt, item)
    item = re.sub("###BLOGURL###", blogpost_url, item)
    item = re.sub("###FILESIZE###", file_size, item)
    item = re.sub("###DURATION###", audio_duration, item)
    item = re.sub("###FILEURL###", file_url, item)
    item = re.sub("###PUBDATE###", pubdate, item)
    item = re.sub("###GUID###", guid, item)
    print(item)