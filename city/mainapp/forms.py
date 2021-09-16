from django import forms


GEEKS_CHOICES = (

    (" ", " "),

    ("с девушкой", "с девушкой"),

    ("с друзьями", "с друзьями"),

    ("с семьей", "с семьей")



)

STATION_CHOICES = (

    (" ", " "),

    ("свиблово", "свиблово"),

    ("выхино", "выхино"),

    ("новогиреево", "новогиреево"),

    ("отрадное", "отрадное"),

    ("таганская", "таганская"),

    ("площадь революции", "площадь революции"),

    ("новокузнецкая", "новокузнецкая"),

    ("медведково", "медведково"),

    ("тургеневская", "тургеневская")

)

PRICE_CHOICES = (

    (" ", " "),

    ("до 800 рублей", "до 800 рублей"),

    ("800-1500", "800-1500"),

    ("1500-2000", "1500-2000"),

    ("2000+", "2000+"),
)


MEAL_CHOICES = (

    ("Китайская" , "Kitay")
)
# создание формы

class GeeksForm(forms.Form):

    geeks_field = forms.ChoiceField(choices=GEEKS_CHOICES)
    station_field = forms.ChoiceField(choices=STATION_CHOICES)
    price_field = forms.ChoiceField(choices=PRICE_CHOICES)
    rating_field = forms.IntegerField(min_value=0, max_value=5)




class CommentForm(forms.Form):
    parent_comment = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False
    )

    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )