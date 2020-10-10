#!/usr/bin/env python3

#
#  floppies - generate color pallettes from images in bulk
#  See the bottom of this file for license information
#

import argparse
import colorgram
from os.path import isfile
from floppies.util import fs
from floppies.util.db import Database


debug_max_images = 10  # Set to 0 to disable limiting # of images processed
debug_force_processing = True

g_files_dbfile = 'database.json'
g_files_image_folder = 'images'
g_files_image_exts = ['.jpg', '.png']
g_processing_num_colors = 10
g_processing_color_threshold = 0.01


if __name__ == '__main__':
    # 1. Get list of image files in images/
    images = fs.enumerate_images(g_files_image_folder, g_files_image_exts)

    if debug_max_images > 0:
        images = images[:debug_max_images]

    print('[main]', 'got', len(images), 'images')

    # 2. Read database if it exists
    db = None
    if isfile(g_files_dbfile):
        db = Database(g_files_dbfile)
    else:
        db = Database()

    # 3. Loop over list of images, extracting their most common colors
    for image in images:
        if not db.add(image, {}, force=debug_force_processing):
            continue

        print('[main]', 'processing', image)

        extracted_colors = colorgram.extract(image, g_processing_num_colors)
        relavent_colors = []

        # 3.2 Filter nosy hex codes (i.e. those that hardly show up)
        for color in extracted_colors:
            if color.proportion > g_processing_color_threshold:
                hex_code = '%02x%02x%02x' % color.rgb
                hex_code = f'#{hex_code}'

                relavent_colors.append(hex_code)

        db.add(image, {'colors': relavent_colors}, force=True)

    print('[main]', 'updated database:')
    print(db)

    db.export_to_file(g_files_dbfile)


#  floppies - generate color pallettes from images in bulk
#  Copyright (C) 2020  Ralph Drake

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.

#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
