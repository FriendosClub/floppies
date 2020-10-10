#  floppies - generate color pallettes from images in bulk
#  See the bottom of this file for license information

import json


g_db_version = 1


class Database(object):
    def __init__(self, filename=None):
        if filename:
            self.import_from_file(filename)
            self.__check_version()
        else:
            self.data = {}
            self.__set_version(g_db_version)

    def __str__(self):
        return json.dumps(self.__data, sort_keys=True, indent=4)

    def __sync(self):
        self.version = self.__data['version']

    def __set_version(self, new_version):
        self.__data['version'] = new_version
        self.__sync()

    def __check_version(self) -> bool:
        if self.get_version() != g_db_version:
            raise Exception('[Database] mismatched database versions.')

    def import_from_file(self, filename):
        # TODO: Error handling
        with open(filename, 'r') as db_file:
            self.__data = json.load(db_file)
        self.__sync()

    def export_to_file(self, filename):
        with open(filename, 'w') as db_file:
            json.dump(self.__data, db_file)
        self.__sync()

    def get_version(self) -> int:
        try:
            return self.__data['version']
        except KeyError as _:
            print('[Database.get_version]', 'no "version" field in database.')
            self.__set_version(g_db_version)

        self.__sync()

    def exists(self, image: str) -> bool:
        return image in self.__data

    def add(self, image: str, data, *, force=False) -> bool:
        if force:
            print('[Database.add]', 'force adding', image)
        elif self.exists(image):
            print('[Database.add]', 'skipping', image)
            return False

        self.__data[image] = data
        print('[Database.add]', 'added', image)
        return True

    def update(self, filename: str, data):
        pass


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
