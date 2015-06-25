# The MIT License (MIT)
#
# Copyright (c) 2013 Marek Mikuliszyn
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# from django.conf import settings
from api.helpers import api_call
from api.models.trade import Trade


@api_call
def index(request, token):
    return Trade(request).get_list()


@api_call
def details(request, token, trade_id):
    return Trade(request).get_trade(trade_id)


@api_call
def for_signal(request, token, signal_id):
    return Trade(request).get_trade_by_signal(signal_id)


@api_call
def open(request, token, trade_id):
    return Trade(request).log_action(trade_id, 'open', '')


@api_call
def fill(request, token, trade_id):
    return Trade(request).log_action(trade_id, 'fill', '')


@api_call
def update(request, token, trade_id):
    return Trade(request).log_action(trade_id, 'update', '')


@api_call
def close(request, token, trade_id):
    return Trade(request).log_action(trade_id, 'close', '')


@api_call
def expired(request, token, trade_id):
    return Trade(request).log_action(trade_id, 'expired', '')


@api_call
def log_info(request, token, trade_id):
    return Trade(request).log_action(trade_id, 'info', '')


@api_call
def log_error(request, token, trade_id):
    return Trade(request).log_action(trade_id, 'error', '')
