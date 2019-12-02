from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Fire (expire) password for users, which have weak password'

    def add_arguments(self, parser):
        self.parser = parser

        parser.add_argument(
            '--all', action='store_true',
            help=('Fire all passwords. use this only if YOU ARE VERY SURE '
                  'such as all passwords are leaked, or all kinds of '
                  'password hashers you use are vulnerable.'),
        )

        parser.add_argument(
            '--hashers', metavar='hasher', type=str, nargs='+',
            help=('Fire passwords for specific hashers you declare. '
                  'Use this when password hasher\'s algorithm is broken.'),
        )

        parser.add_argument(
            '--users', metavar='user_id', type=int, nargs='+',
            help=('It deletes password for specific users. Use this '
                  'when some user\'s password is leaked. '
                  'e.g.) their passwords are littered public sites.'),
        )

    def handle(self, *args, **kwargs):
        if kwargs['all']:
            # fire all passwords
            pass

        elif kwargs['hashers']:
            # fire passwords for hashers
            pass

        elif kwargs['users']:
            # fire passwords for users
            pass

        else:
            self.parser.print_help()
            raise CommandError('Select one of options. all, hashers or users')
