#!/bin/env python

# Need ffmpeg on path
import ffmpeg,os,shutil
from dateutil import parser

for f in os.listdir('.'):
  print (f)
  try:
      probe = ffmpeg.probe(f)
      creationDate = parser.parse(probe['format']['tags']['creation_time'])
      shutil.move(f,'d:/Videos/{}'.format(creationDate.year))
  except Exception as e:
        print (e)
        shutil.move(f,'../junk')