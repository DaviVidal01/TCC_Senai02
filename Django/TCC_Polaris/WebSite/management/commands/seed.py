from django.core.management.base import BaseCommand
from Website.seeder import DadosHighFashionBD

class Command(BaseCommand):
    help = 'Preenche o banco de dados com dados de exemplo.'

    def handle(self, *args, **options):
        DadosHighFashionBD()
        self.stdout.write(self.style.SUCCESS('Dados foram criados com sucesso.'))