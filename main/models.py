from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Customer(AbstractUser):
    user_name = models.CharField(max_length=200, null=True, default='Анонім')
    city = models.CharField(max_length=200, null=True, default="Kyiv")
    street = models.CharField(max_length=200, null=True)
    house = models.CharField(max_length=200, null=True)
    apartment = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=False)
    is_confirmed = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Клієнт"
        verbose_name_plural = "Клієнти"


class Staff(Customer):
    salary = models.IntegerField(null=True, default=0)
    percent = models.CharField(max_length=100, null=True, default=0)
    start_work = models.DateTimeField(auto_now_add=True)
    faired = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Працівник"
        verbose_name_plural = "Працівники"


class Confirmations(models.Model):
    user_ref = models.ForeignKey(Customer, on_delete=models.CASCADE)
    confirmation_key = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="task_client", null=True)
    anonim_user = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True, default="Київ")
    street = models.CharField(max_length=200, null=True)
    house = models.CharField(max_length=200, null=True)
    apartment = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=1000, null=False)
    created = models.DateTimeField(auto_now_add=True)
    in_work = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    employee = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, related_name="task_employee")
    price = models.IntegerField(null=True, default=0)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Price(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="price_category")
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Прайс"
        verbose_name_plural = "Прайс"


class CallBack(models.Model):
    name = models.CharField(max_length=200, default="Анонімний користувач")
    phone = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Зворотній дзвінок"
        verbose_name_plural = "Зворотні дзвінки"


class Feedback(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    client = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, related_name="feedback")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], choices=RATING_CHOICES)
    comment = models.CharField(max_length=1000, null=True, default='')

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
