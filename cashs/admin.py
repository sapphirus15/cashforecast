from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from . import models


admin.site.site_header = "Neuromeka - Cash Flow Forecasting"

@admin.register(models.Cash)
class CashAdmin(admin.ModelAdmin):

    list_display = (
        "date",
        "cash_type", 
        "item", 
        "classfication", 
        "op_month", 
        "amount",
        "created_date",
        "updated_date"

    )

    list_filter = (
        ("date", DateRangeFilter), 
        "cash_type"
    )

    search_fields = ("date", "cash_type", "item")

