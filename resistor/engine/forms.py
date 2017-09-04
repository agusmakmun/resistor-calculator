from django import forms

OPTIONS_COLOR_CODE = (
    (0, 'Black'), (1, 'Brown'), (2, 'Red'), (3, 'Orange'), (4, 'Yellow'),
    (5, 'Green'), (6, 'Blue'), (7, 'Purple'), (8, 'Gray'), (9, 'White')
)

OPTIONS_COLOR_CODE_DOUBLE = (
    (0, 'Black'), (1, 'Brown'), (2, 'Red'), (3, 'Orange'),
    (4, 'Yellow'), (5, 'Green'), (6, 'Blue'), (7, 'Purple'),
    (8, 'Gray'), (9, 'White'), ('-1', 'Gold'), ('-2', 'Silver')
)

OPTIONS_RESISTANCE_4_BRACERLET = (
    ('None', 'Other Colors'), ('5%', 'Gold'),
    ('10%', 'Silver'), ('20%', 'No Color')
)

OPTIONS_RESISTANCE_5_BRACERLET = (
    ('None', 'Other Colors'), ('1%', 'Brown'), ('2%', 'Red'),
    ('0.5%', 'Green'), ('0.25%', 'Blue'), ('0.1%', 'Purple'),
    ('5%', 'Gold'), ('10%', 'Silver'),
)


class Resistor4BraceletsForm(forms.Form):
    attrs = {'class': 'form-control cs-max-4'}

    color_1 = forms.ChoiceField(
        widget=forms.Select(attrs=attrs),
        choices=OPTIONS_COLOR_CODE)

    color_2 = forms.ChoiceField(
        widget=forms.Select(attrs=attrs),
        choices=OPTIONS_COLOR_CODE)

    color_3 = forms.ChoiceField(
        widget=forms.Select(attrs=attrs),
        choices=OPTIONS_COLOR_CODE_DOUBLE)

    color_4 = forms.ChoiceField(
        widget=forms.Select(attrs=attrs),
        choices=OPTIONS_RESISTANCE_4_BRACERLET)


class Resistor5BraceletsForm(forms.Form):
    attrs = {'class': 'form-control cs-max-5'}

    color_1 = forms.ChoiceField(
        widget=forms.Select(attrs=attrs),
        choices=OPTIONS_COLOR_CODE)

    color_2 = forms.ChoiceField(
        widget=forms.Select(attrs=attrs),
        choices=OPTIONS_COLOR_CODE)

    color_3 = forms.ChoiceField(
        widget=forms.Select(attrs=attrs),
        choices=OPTIONS_COLOR_CODE)

    color_4 = forms.ChoiceField(
        widget=forms.Select(attrs=attrs),
        choices=OPTIONS_COLOR_CODE_DOUBLE)

    color_5 = forms.ChoiceField(
        widget=forms.Select(attrs=attrs),
        choices=OPTIONS_RESISTANCE_5_BRACERLET)
