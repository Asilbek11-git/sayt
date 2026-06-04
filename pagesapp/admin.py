from django.contrib import admin,messages
from .models import Muallif, Janr,Kitob,KitobNusxa,Ijara

admin.site.register(Muallif)
admin.site.register(Janr)










class KitobNusxaInline(admin.TabularInline):
    model = KitobNusxa
    extra = 1  



@admin.action(description="Tanlanganlarni mavjud deb belgilash")
def make_available(modeladmin, request, queryset):
    updated = queryset.update(mavjud=True)
    modeladmin.message_user(
        request,
        f"{updated} ta kitob muvaffaqiyatli 'Mavjud' deb belgilandi.",
        messages.SUCCESS,
    )


@admin.action(description="Narxni 10% tushirish")
def discount_price(modeladmin, request, queryset):
    count = 0
    for kitob in queryset:

        kitob.narx = kitob.narx * 0.9
        kitob.save()
        count += 1
    modeladmin.message_user(
        request,
        f"{count} ta kitobning narxi 10% ga arzonlashtirildi.",
        messages.SUCCESS,
    )



@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display  = ('nomi', 'muallif', 'nashr_yili', 'narx', 'mavjud')
    list_filter   = ('mavjud', 'til', 'janrlar', 'nashr_yili')
    search_fields = ('nomi', 'muallif__ism')   
    ordering   = ('-nashr_yili',)   

readonly_fields = ('qoshilgan_sana',)

fieldsets = (
    ('Asosiy ma\'lumot', {
    'fields': ('nomi', 'muallif', 'janrlar'),
    }),
    ('Qo\'shimcha', {
    'fields': ('til', 'nashr_yili', 'narx', 'mavjud', 'qoshilgan_sana'),
    'classes': ('collapse',),
    }),
)
list_per_page= 20


inlines = [KitobNusxaInline] 
actions = [make_available,discount_price]


