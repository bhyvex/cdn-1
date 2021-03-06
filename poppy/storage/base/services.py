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

import abc
import six

from poppy.storage.base import controller


@six.add_metaclass(abc.ABCMeta)
class ServicesControllerBase(controller.StorageControllerBase):

    def __init__(self, driver):
        super(ServicesControllerBase, self).__init__(driver)

    @abc.abstractmethod
    def list(self, project_id, marker=None, limit=None):
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, project_id, service_name, service_json):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, project_id, service_name, service_json):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, project_id, service_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self):
        raise NotImplementedError
