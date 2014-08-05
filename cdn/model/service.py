# Copyright (c) 2014 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Service(object):

    def __init__(self, name, domains, origins):
        self._name = name
        self._domains = domains
        self._origins = origins
        self._caching = []
        self._restrictions = []
        self._links = []

    @property
    def name(self):
        return self._name

    @property
    def domains(self):
        return self._domains

    @property
    def origins(self):
        return self._origins

    @property
    def caching(self):
        return self._caching

    @property
    def restrictions(self):
        return self._restrictions

    @property
    def links(self):
        return self._links
