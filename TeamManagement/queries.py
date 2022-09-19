from .models import *


def company_query():
    return Company.objects.all()


def company_name_filter_query(name):
    return Company.objects.filter(company_name__icontains=name)


def company_id_filter_query(id):
    return Company.objects.get(id=id)

def team_query():
    return Team.objects.all()
