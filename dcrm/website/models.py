from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    STATE_CHOICES = [
        ("BW", "Baden-Württemberg"),
        ("BY", "Bayern"),
        ("BE", "Berlin"),
        ("BB", "Brandenburg"),
        ("HB", "Bremen"),
        ("HH", "Hamburg"),
        ("HE", "Hessen"),
        ("MV", "Mecklenburg-Vorpommern"),
        ("NI", "Niedersachsen"),
        ("NW", "Nordrhein-Westfalen"),
        ("RP", "Rheinland-Pfalz"),
        ("SL", "Saarland"),
        ("SN", "Sachsen"),
        ("ST", "Sachsen-Anhalt"),
        ("SH", "Schleswig-Holstein"),
        ("TH", "Thüringen"),
    ]

    state = models.CharField(
        max_length=2, 
        choices=STATE_CHOICES,
        default="BY"  # optional: set a default value
    )
    
    zipcode = models.CharField(max_length = 20)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")