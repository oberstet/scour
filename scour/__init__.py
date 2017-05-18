###############################################################################
#
# Copyright (C) 2010 Jeff Schiller, 2010 Louis Simard, 2013-2015 Tavendo GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
###############################################################################


from .version import __version__


# public API
from .scour import scourString as scour_string
from .scour import scourXmlFile as scour_xml_file
from .scour import sanitizeOptions as options
from .scour import parse_args

__all__ = ['scour_string', 'scour_xml_file', 'options', 'parse_args']


# silence pyflakes
version = __version__
