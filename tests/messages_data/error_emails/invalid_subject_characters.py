import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Formao FrenetikPolis: Mega Campanha Final Vero | Cursos de Setembro',
    from_='info@formacaofrenetik.info',
    to=('martin@internet.ao', 'iris@internet.ao', 'support@maxnet.ao'),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1900, 1, 1, 0, 0),
    date_str='',
    text='TEST\r\n',
    html='',
    headers={'from': ('"=?Windows-1252?B?Rm9ybWHn428gRnJlbmV0aWtwb2xpcw==?=" <info@formacaofrenetik.info>',), 'to': ('martin@internet.ao, iris@internet.ao, support@maxnet.ao',), 'subject': ('Forma\udce7\udce3o FrenetikPolis: Mega Campanha Final Ver\udce3o | Cursos de Setembro',)},
    attachments=[],
    from_values=EmailAddress('Formação Frenetikpolis', 'info@formacaofrenetik.info', 'Formação Frenetikpolis <info@formacaofrenetik.info>'),
    to_values=(EmailAddress('', 'martin@internet.ao', 'martin@internet.ao'), EmailAddress('', 'iris@internet.ao', 'iris@internet.ao'), EmailAddress('', 'support@maxnet.ao', 'support@maxnet.ao')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)