from django.contrib.admin import SimpleListFilter

class PriceFilter(SimpleListFilter):
    title ="Price Range"
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return [
            ('low', 'Low < 50'),
            ('high', 'High > 50')
        ]
    
    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(price__lt=50)
        if self.value() == 'high':
            return queryset.filter(price__gt=50)
        return queryset