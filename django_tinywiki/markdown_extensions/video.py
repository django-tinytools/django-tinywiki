from markdown.inlinepatterns import InlineProcessor
from markdown import extensions
from xml.etree import ElementTree as etree

from django.shortcuts import reverse
from django.utils.html import escape

import os

class YoutubeVideoInlineProcessor(InlineProcessor):
    def handleMatch(self,m,data):
        title=m.group(1)
        video_id=m.group(3)

        element = etree.Element("iframe",attrib={
            'width': '560',
            'height': '315',
            'src':'https://www.youtube.com/embed/{video_id}'.format(video_id=video_id),
            'title': title,
            'frameborder': '0',
            'allow': "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share",
            'allowfullscreen':"",
        })

        return element, m.start(0), m.end(0)

VIDEO_TYPES={
    '.asf': 'video/x-ms-asf',
    '.avi': 'video/x-msvideo',
    '.mp4': 'video/mp4',
    '.m4v': 'video/x-m4v',
    '.mgp': 'video/mpeg',
    '.ogg': 'video/ogg',
    '.flv': 'video/x-flv',
    '.m3u8': 'application/x-mpegURL',
 	'.ts':  'video/MP2T',
    '.3gp':	'video/3gpp',
    '.mov':	'video/quicktime',
    '.qt': 'video/quicktime',
    '.wmv': 'video/x-ms-wmv',
    '.webm': 'video/webm'

}

class VideoInlineProcessor(InlineProcessor):
    def handleMatch(self,m,data):
        title=m.group(1)
        video_data=m.group(2).split('|')
        print(video_data)
        video_src = video_data[0]
        video_attrib={'controls':'1'}
        source_attrib = {'src':video_src}

              
        if len(video_data) >= 2:
            if video_data[1]:
                video_size=video_data[1].split(',')
                video_attrib['width'] = video_size[0]
                if len(video_size) >= 1:
                    video_attrib['height'] = video_size[1]
        if len(video_data) >= 3:
            for i in video_data[2:]:
                if not i.strip():
                    continue
                if '=' in i:
                    attr,value = i.strip().split('=')
                else:
                    attr=i.strip()
                    value=""

                video_attrib[attr]=value
                
        fname,fext=os.path.splitext(video_src)
        if fext in VIDEO_TYPES:
            source_attrib['type'] = VIDEO_TYPES[fext]


        element = etree.Element("video",attrib=video_attrib)
        element.append(etree.Element("source",attrib=source_attrib))
        element.text=title

        return element, m.start(0), m.end(0)

class VideoExtension(extensions.Extension):
    def extendMarkdown(self,md):
        YT_LINK_PATTERN = "\?\[(.*?)\]\((yt|youtube):(.+?)\)"
        VIDEO_LINK_PATTERN = "\?\[(.*?)\]\((.+?)\)"

        md.inlinePatterns.register(YoutubeVideoInlineProcessor(YT_LINK_PATTERN,md),"youtube-video",175)
        md.inlinePatterns.register(VideoInlineProcessor(VIDEO_LINK_PATTERN,md),"video",170)