# Copyright (C) 2013-2014 Fox Wilson, Peter Foley, Srijay Kasturi, Samuel Damashek, James Forcier and Reed Koser
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import subprocess
import random
import os
from cslbot.helpers.command import Command


@Command(['brain'], limit=1)
def cmd(send, msg, args):
    """Neural networks!
    Syntax: !brain
    """
    # FIXME: this whole thing is a god-awful hack
    f = next(reversed((sorted(os.listdir('/home/peter/char-rnn/cv')))))
    send(f)
    seed = str(random.randint(0,100000))
    output = subprocess.check_output(['/home/peter/torch/install/bin/th', 'sample.lua',
        '/home/peter/char-rnn/cv/%s' % f, '-gpuid', '-1', '-seed', seed], cwd='/home/peter/char-rnn').decode('utf-8', 'ignore').splitlines()
    lines = [line.strip() for line in output[2:]]
    for line in sorted(lines, key=len, reverse=True):
        send(line)
