#   Copyright 2017 Intel, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

"""OpenStackClient plugin for RSD(Rack Scale Design)."""

import logging

from osc_lib import utils

LOG = logging.getLogger(__name__)

DEFAULT_API_VERSION = '1'
API_VERSION_OPTION = 'os_rsd_api_version'
API_NAME = 'rsd'
API_VERSIONS = {
    '1': 'rsdclient.v1.client.Client',
}


def make_client(instance):
    """Returns a rsd client."""
    rsd_client = utils.get_client_class(
        API_NAME,
        instance._api_version[API_NAME],
        API_VERSIONS)
    LOG.debug('Instantiating RSD client: %s', rsd_client)

    client = rsd_client(base_usr="https://localhost:8442/redfish/v1/",
                        username="admin",
                        password="admin",
                        verify=False)
    return client


def build_option_parser(parser):
    """Hook to add global options"""

    parser.add_argument(
        '--os-rsd-api-version',
        metavar='<rsd-api-version>',
        default=utils.env(
            'OS_RSD_API_VERSION',
            default=DEFAULT_API_VERSION),
        help='RSD API version, default=' +
             DEFAULT_API_VERSION +
             ' (Env: OS_RSD_API_VERSION)')
    return parser
