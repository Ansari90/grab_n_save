__author__ = 'Abdullah AA'

from html.parser import HTMLParser


class ImageParser(HTMLParser):
    image_links = []
    image_names = []

    def handle_starttag(self, tag, attrs):
        target_found = False

        if tag == 'a':
            for temp_tuple in attrs:
                if temp_tuple[0] == 'class' and temp_tuple[1] == 'fileThumb':
                    target_found = True

        if target_found:
            for temp_tuple in attrs:
                if temp_tuple[0] == 'href':
                    self.image_links.append(temp_tuple[1])

    def set_image_name(self):
        for link in self.image_links:
            big_image_name = list(link)
            counter = len(big_image_name) - 1
            regular_image_name = ''

            while big_image_name[counter] != '/':
                counter -= 1
            counter += 1

            while counter < len(big_image_name):
                regular_image_name += big_image_name[counter]
                counter += 1

            self.image_names.append(regular_image_name)