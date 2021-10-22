#!/bin/env python
from PIL import Image
import os,shutil
from PIL.ExifTags import TAGS
from datetime import datetime

def listTags(exifdata):
    d = None
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        if tag != 'DateTime': continue
        data = exifdata.get(tag_id)
        # decode bytes 
        if isinstance(data, bytes):
            data = data.decode()
        print ('{}:{}'.format(tag,data))
        d = data
        break
    return d


for f in os.listdir('.'):
  try:
      image = Image.open(f)
      creationDate = listTags( image.getexif() )
      if creationDate is None: raise Exception("Cannot find exif for {}".format(f) )
      creationDate = datetime.strptime( creationDate, '%Y:%m:%d %H:%M:%S')
      image.close()
      shutil.move(f,'d:/Pictures/{}'.format(creationDate.year))
  except Exception as e:
        image.close()
        print (e)
        shutil.move(f,'../junk')