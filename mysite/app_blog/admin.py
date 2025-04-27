from django.contrib import admin
from .models import Article, Category, ArticleImage
from .forms import ArticleImageForm
from django.shortcuts import get_object_or_404

# Реєстрація моделі Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}
    fieldsets = (
        ('', {
            'fields': ('category', 'slug'),
        }),
    )

admin.site.register(Category, CategoryAdmin)

# Інлайн для зображень
class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fieldsets = (
        ('', {
            'fields': ('title', 'image',),
        }),
    )

# Налаштування адміністративної панелі для Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    inlines = [ArticleImageInline]
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('category',)
    fieldsets = (
        ('', {
            'fields': ('pub_date', 'title', 'description', 'main_page'),
        }),
        (u'Додатково', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug',),
        }),
    )

    def delete_file(self, pk, request):
        '''Delete an image.'''
        obj = get_object_or_404(ArticleImage, pk=pk)
        return obj.delete()

# Ось тут ви реєструєте модель Article разом з ArticleAdmin
admin.site.register(Article, ArticleAdmin)
