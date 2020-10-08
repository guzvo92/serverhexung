
#[ADMIN / Watchlist]

from django.contrib import admin
from .models import *

admin.site.register(Chareg)
admin.site.register(Charsadminwatchlist)


title = "Admin Nocteam"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de Gestion"
