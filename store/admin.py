from django.contrib import admin
from django.utils import timezone

# Register your models here.
from .models import Game, GameImage

def draft_status(modeladmin, request, queryset):
    queryset.update(
        draft=False,
        upload_date=timezone.now()
    )
draft_status.short_description = 'Mark Game as released now' # at admin page




#lass GameImageInline(admin.TabularInline):
#    model = GameImage
#    extra = 2 # optional : show 2 items (default = 3)


class GameInline(admin.StackedInline):
    model = Game
    extra = 1  # show only one item

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):

    list_display = ['title', 'category', 'upload_date',
                                 'updated']

    search_fields = ['title']
    actions = [draft_status]
    date_hierarchy = 'upload_date'
    prepopulated_fields = {'slug': ('title',)}

    # both 'fields' and 'fieldsets' can not be specified together
    fieldsets = (
            (None, {  # label 1: None
                'fields': ( # dictionary
                    ('title', 'slug'),
                )
            }),
            ('More details', { # under label 2 : More details
                'classes': ('collapse',),  # css-class : minimized
                'fields': (

                    'descriptipn',
                    ( 'upload_date'),
                )
            })
        )
    #inlines = [GameImageInline]




#admin.site.register(GameImage)
# admin.site.register(Publisher)
