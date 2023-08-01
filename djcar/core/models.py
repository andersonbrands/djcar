from django.db import models


# Create your models here.
class Car(models.Model):
    BRANDS = (
        ("ford", "Ford"),
        ("chevy", "Chevy"),
        ("toyota", "Toyota"),
        ("volks", "Volks"),
    )
    COLORS = (
        ("red", "Red"),
        ("blue", "Blue"),
        ("black", "Black"),
        ("yellow", "Yellow"),
        ("white", "White"),
    )
    model = models.CharField(max_length=45)
    brand = models.CharField(max_length=45, choices=BRANDS)
    main_color = models.CharField(max_length=25, choices=COLORS)
    value = models.PositiveIntegerField()
    production_cost = models.PositiveIntegerField()
    transportation_cost = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.model} - {self.brand} ({self.main_color})"
