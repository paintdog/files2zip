#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import os
import zipfile

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

modes = {zipfile.ZIP_DEFLATED: 'deflated',
         zipfile.ZIP_STORED:   'stored',
         }

zf = zipfile.ZipFile('__d 2 -- {}.zip'.format(datetime.date.today()), mode='w')
try:
    for file in [file for file in os.listdir() if file.endswith(".jpg") and os.path.isfile(file)]:
        zf.write(file, compress_type=compression)
finally:
    zf.close()

