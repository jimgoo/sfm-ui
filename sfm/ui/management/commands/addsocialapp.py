from django.core.management.base import BaseCommand
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site


class Command(BaseCommand):
    help = 'Creates a Social App if it does not exist.'

    def add_arguments(self, parser):
        parser.add_argument('provider')
        parser.add_argument('client_id', nargs='?')
        parser.add_argument('secret', nargs='?')

    def handle(self, *args, **options):
        if options['client_id'] and options['secret']:
            app = SocialApp.objects.filter(provider=options['provider'])
            if not app.exists():
                social_app = SocialApp.objects.create(provider=options['provider'],
                                                      client_id=options['client_id'],
                                                      secret=options['secret'],
                                                      name=options['provider'])
                site = Site.objects.all()[0]
                assert site
                social_app.sites.add(site)
                site.save()
                self.stdout.write('Created {} social app.'.format(options['provider']))
            else:
                #app.client_id = options['client_id']
                #app.secret = options['secret']
                #app.save() # QuerySet cannot be saved
                self.stdout.write(
                    'Skipping creating {} social app since it already exists.'.format(options['provider']))

        else:
            self.stdout.write('Skipping creating {} social app.'.format(options['provider']))
