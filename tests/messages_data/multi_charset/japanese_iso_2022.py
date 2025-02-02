import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='まみむめも',
    from_='raasdnil@gmail.com',
    to=('raasdnil@gmail.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1900, 1, 1, 0, 0),
    date_str='',
    text='すみません。\r\n\r\n',
    html='',
    headers={'mime-version': ('1.0',), 'subject': ('=?UTF-8?B?44G+44G/44KA44KB44KC?=',), 'from': ('Mikel Lindsaar <raasdnil@gmail.com>',), 'to': ('=?UTF-8?B?44G/44GR44KL?= <raasdnil@gmail.com>',), 'content-type': ('text/plain;\r\n charset=iso-2022-jp',), 'content-transfer-encoding': ('7bit',)},
    attachments=[],
    from_values=EmailAddress('Mikel Lindsaar', 'raasdnil@gmail.com', 'Mikel Lindsaar <raasdnil@gmail.com>'),
    to_values=(EmailAddress('みける', 'raasdnil@gmail.com', 'みける <raasdnil@gmail.com>'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)