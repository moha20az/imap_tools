import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Redacted',
    from_='redacted@flashmail.net',
    to=('redacted@Enron.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1900, 1, 1, 0, 0),
    date_str='',
    text='',
    html='<p>foo</p>\n',
    headers={'from': ('<redacted@flashmail.net>',), 'subject': ('Redacted',), 'to': ('<redacted@Enron.com>',), 'message-id': ('<105647271315.NCV17523@x263.net>',), 'mime-version': ('1.0',), 'content-type': ('text/html;\n charset=utf-8',), 'content-disposition': ('=?utf-8?Q?invalid?=', '=?utf-8?Q?invalid?='), 'content-transfer-encoding': ('quoted-printable',)},
    attachments=[],
    from_values=EmailAddress('', 'redacted@flashmail.net', 'redacted@flashmail.net'),
    to_values=(EmailAddress('', 'redacted@Enron.com', 'redacted@Enron.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)