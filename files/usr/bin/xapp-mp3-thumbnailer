#!/usr/bin/python3

import sys
import eyed3
import XappThumbnailers

thumbnailer = XappThumbnailers.Thumbnailer()

try:
    audio_file = eyed3.load(thumbnailer.args.input)
    if audio_file.tag.images != None and len(audio_file.tag.images) > 0:
        thumbnailer.save_bytes(audio_file.tag.images[0].image_data)
        sys.exit(0)
except AttributeError as e: # (audio_file is None)
    pass
except Exception as e:
    print(e)

sys.exit(1)