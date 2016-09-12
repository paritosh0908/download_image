"""
reads text file containing urls and downloads images to the current directory
can be run as <python download_images.py /home/user/foo/bar/links.txt>
writes logs to /tmp/download_images.log
"""
#!/usr/bin/python

import sys
import requests
import logging
import traceback

logging.basicConfig(filename='/tmp/download_images.log',level=logging.INFO)

def parse_file(link_file):
    logging.info('Got file %s' % link_file)
    urls = open(link_file,'r')
    file_iter = 1

    for url in urls:
        # iterating over file line by line
        try:
            logging.info('Trying to download from url : %s' % url)
            url_f = url.strip('\n')
            image_name = str(file_iter) + '.' + url_f[url_f.rfind('.') + 1:]
            # image_name set as integers starting with 1 appended with the
            # appropriate file extension (1.jpg, 2.png)
            f = open(image_name, 'wb')
            response = requests.get(url_f)
            # -1 to ignore the newline character at the end of string
            logging.info("Got response code %s" % response)
            f.write(response.content)
            f.close()
            logging.info("Successfully wrote to file %s" % image_name)
            file_iter+=1
        except:
            logging.exception("Got exception while trying to fetch file %s"
                              % traceback.format_exc())
    urls.close()

if __name__=='__main__':
    parse_file(sys.argv[1])
