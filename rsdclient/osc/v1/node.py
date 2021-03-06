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

import os

from osc_lib.command import command


class ComposeNode(command.Command):
    _description = "Compose a Node"

    def get_parser(self, prog_name):
        parser = super(ComposeNode, self).get_parser(prog_name)
        # NOTE: All arguments are positional and, if not provided
        # with a default, required.
        parser.add_argument('--name',
                            dest='name',
                            required=True,
                            metavar='<name>',
                            help='Name of the composed node.')
        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)

        print("Request to compose node %s was accepted"
              % parsed_args.name)
