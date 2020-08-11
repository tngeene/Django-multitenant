from django.db import connection
from .models import Tenant

def hostname_from_request(request):
    # split on ':' to remove port
    return request.get_host().split(":")[0].lower()


def tenant_db_from_request(request):
    hostname = hostname_from_request(request)
    tenants_map = get_tenants_map()
    return tenants_map.get(hostname)


def get_tenants_map():
    tenant_dict = dict(Tenant.objects.values_list("subdomain","schema_name").distinct())
    print(f"I am {tenant_dict}")
    return tenant_dict
    # tenant_dict = {'ngeene.localhost': 'ngeene', 'skye.localhost': 'skye'}
    # print(f"I am the {tenant_dict}")
    # return tenant_dict