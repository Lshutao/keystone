# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_context import context as oslo_context


REQUEST_CONTEXT_ENV = 'keystone.oslo_request_context'


def _prop(name):
    return property(lambda x: getattr(x, name),
                    lambda x, y: setattr(x, name, y))


class RequestContext(oslo_context.RequestContext):

    def __init__(self, **kwargs):
        self.project_name = kwargs.pop('project_name', None)
        self.domain_name = kwargs.pop('domain_name', None)
        self.username = kwargs.pop('username', None)
        self.user_domain_name = kwargs.pop('user_domain_name', None)
        self.project_domain_name = kwargs.pop('project_domain_name', None)
        super(RequestContext, self).__init__(**kwargs)

    @classmethod
    def from_environ(cls, environ, **kwargs):
        kwargs.setdefault('request_id', environ.get('openstack.request_id'))
        return super(RequestContext, cls).from_environ(environ, **kwargs)

    user_id = _prop('user')
    project_id = _prop('tenant')
    domain_id = _prop('domain')
    user_domain_id = _prop('user_domain')
    project_domain_id = _prop('project_domain')
