from django.core.management.base import BaseCommand
from product.models import Subscribers


SUBS = [
 'sd@df.com',
 'cvvc@jksfnks.com',
 'jmsdjsmd@jhsfs',
 'sd@jmsdsk',
 'dsd@dsfs',
 'dsdsd@sfsf',
 'dsdsd@sfds',
 'dshjdjh@jhsj',
 'ajhdj@jnhasdjs',
 'sad@dsdfs',
 'sds@sfs',
 'dsd@dfgdg',
 'df@dsfc',
 'sdsn@xssdc',
 'xxxx@dxsd',
 'dsd@sfsf',
 'sas@dsds',
 'dad@sds',
 'asas@sds',
 'ww@dsd',
 'xxx@csfds.sds',
 'cxcxc@jhsds',
 'xchjn@hjshd',
 'xcx@dsdf',
 'ccc@jshds',
 'jchvjc@hjshdj',
 'asa@gmail.com',
 'xxxx@dsd',
 'cc@ff',
 'nb',
 'jhj',
 'gj',
 'cc',
 'c',
 'cc',
 'jhj',
 'hhh',
 'ccccccc',
 'ffff',
 'cccc',
 'query@gih.com',
 'ccc',
 'cc',
 'dsdsd@gmail.com',
 'qwert@gih.com',
 'qwer@gih.com',
 'test@foobar.com']


class Command(BaseCommand):
    help = 'Delete all products.'


    def handle(self, *args, **kwargs):
        Subscribers.objects.filter(email__in=SUBS).delete()
