__author__ = 'Abdullah AA'

import urllib.request
import ResponseParser
import io


class ImageGrabber():
    @staticmethod
    def grab_images(page_name):
        response_page = urllib.request.urlopen(page_name)
        parser = ResponseParser.ImageParser(strict=False)

        response_body = response_page.read()
        parser.feed(response_body.decode('utf-8'))
        parser.set_image_name()

        image_links = parser.image_links
        image_names = parser.image_names

        counter = 0
        for link in image_links:
            image_bytes = urllib.request.urlopen('http:' + link).read()
            f = io.open('C:\\Users\\Abdullah AA\\FourChanImages\\' + image_names[counter], 'wb')
            f.write(image_bytes)
            counter += 1