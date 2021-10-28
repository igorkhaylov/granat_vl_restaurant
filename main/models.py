from django.db import models


ITEM_CHOICES = [
    ('snacks', 'Закуски'),
    ('salads', 'Салаты'),
    ('soups', 'Супы'),
    ('hotdishes', 'Горячие блюда'),
    ('bakery', 'Выпечка'),
    ('mangal', 'Мангал'),
    ('sadj', 'Саджи'),
    ('sweets', 'Десерты'),
    ('bar', 'Бар'),
    ('nastoi', 'Настойки')
]


class Products(models.Model):
    title = models.CharField("Название", max_length=120)
    categories = models.CharField('Категория', choices=ITEM_CHOICES, max_length=25)
    slug = models.SlugField("slug", unique=True)
    picture = models.ImageField("Картинка", upload_to='pictures/%Y/%m/%d/')
    description = models.TextField("Описание", max_length=250)
    price = models.IntegerField("Цена", )
    new_products = models.BooleanField("Новинка", )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Mеню"
        ordering = ("-id", )


class MainPicture(models.Model):
    # Главная картинка
    title = models.CharField("Название", max_length=120, default="Главная картинка и О нас")
    picture = models.ImageField('Главная картинка', upload_to="main_picture/%Y/%m/%d/")
    # О нас
    picture1 = models.ImageField('Первая картинка', upload_to="about_us/%Y/%m/%d/")
    description1 = models.TextField('Первое описание', max_length=500)
    picture2 = models.ImageField('Вторая картинка', upload_to="about_us/%Y/%m/%d/")
    description2 = models.TextField('Второе описание', max_length=500)
    picture3 = models.ImageField('Третья картинка', upload_to="about_us/%Y/%m/%d/")
    description3 = models.TextField('Третье описание', max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Главная картинка и О нас"
        verbose_name_plural = "Главная картинка и О нас"
