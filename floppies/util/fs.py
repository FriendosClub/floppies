#  floppies - generate color pallettes from images in bulk
#  See the bottom of this file for license information

import logging
import os


logger = logging.getLogger(__name__)


def enumerate_images(folder: str, type_filter: [str]) -> [str]:
    images = []

    for subdir, _, files in os.walk('images'):
        for filename in files:
            filepath = subdir + os.sep + filename
            _, ext = os.path.splitext(filepath)

            if ext in type_filter:
                images.append(filepath)
            else:
                logger.debug('Skipped %s', filepath)

    return images


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
