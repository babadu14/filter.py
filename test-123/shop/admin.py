from django.contrib import admin
from shop.models import Category, Item, Tag
from shop.filters import PriceFilter

# Register your models here.
# class ItemInline(admin.TabularInline):
#     model = Item
#     extra = 1

class ItemInline(admin.StackedInline):
    model = Item
    extra = 1

class TagItemInline(admin.StackedInline):
    model = Item.tags.through
    extra = 1

class TagInline(admin.StackedInline):
    model = Tag.items.through
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_five_items']
    search_fields = ['name', 'id','items__name']
    ordering = ['name','id']
    list_per_page = 100
    inlines = [ItemInline]

    def get_five_items(self, category):
        items =  category.items.all()
        empty_list = []
        for item in items:
            empty_list.append(item.name)
        return empty_list
    
    def get_queryset(self, request):
        existing_queryset = super().get_queryset(request)
        return existing_queryset.prefetch_related('items')



class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    search_fields = ['name']
    ordering = ['price']
    autocomplete_fields = ['category'] 
    fields = ['name','category', 'price','description', ]
    inlines = [TagInline]
    list_filter = [PriceFilter]
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    autocomplete_fields = ['items']
    inlines = [TagItemInline] 

admin.site.register(Tag, TagAdmin)

admin.site.register(Item, ItemAdmin)

admin.site.register(Category, CategoryAdmin)