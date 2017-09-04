import json
from django.shortcuts import render
from django.http import HttpResponse

from resistor.engine.forms import (
    Resistor4BraceletsForm, Resistor5BraceletsForm)


def resistor_form_view(request):
    """
    Engine of resistor form view.

    the forms:
        - Resistor4BraceletsForm()
        - Resistor5BraceletsForm()

    method:
        - GET : form view.
        - POST: JSON (calculation, tolerance, colors, plain)
    """
    if request.method == 'POST':
        form4bracelet = Resistor4BraceletsForm(request.POST)
        form5bracelet = Resistor5BraceletsForm(request.POST)

        if form4bracelet.is_valid():
            color_1 = form4bracelet.cleaned_data['color_1']
            color_2 = form4bracelet.cleaned_data['color_2']
            color_3 = form4bracelet.cleaned_data['color_3']
            color_4 = form4bracelet.cleaned_data['color_4']

            zero_value = ['0' for x in range(int(color_3))]
            calculation = color_1 + color_2 + ''.join(zero_value)

            if color_3 == '-1':
                calculation = '%s.%s' % (color_1, color_2)
            elif color_3 == '-2':
                calculation = '0.%s%s' % (color_1, color_2)

            if len(calculation) > 3 and color_3 != '-2':
                formatted = format(int(calculation), ',d')
                calculation = '.'.join(formatted.split(','))

            tolerance = color_4
            if tolerance == 'None':
                tolerance = ''
            tolerance_text = '' if tolerance == '' else '~ with tolerance +/- : %s' % tolerance

            data = {
                'calculation': calculation,
                'tolerance': tolerance,
                'colors': [
                    {'color_1': color_1},
                    {'color_2': color_2},
                    {'color_3': color_3},
                    {'color_4': color_4}
                ],
                'plain': '%s Ohm %s' % (calculation, tolerance_text)
            }
            return HttpResponse(json.dumps(data),
                                content_type='application/json')

        if form5bracelet.is_valid():
            color_1 = form5bracelet.cleaned_data['color_1']
            color_2 = form5bracelet.cleaned_data['color_2']
            color_3 = form5bracelet.cleaned_data['color_3']
            color_4 = form5bracelet.cleaned_data['color_4']
            color_5 = form5bracelet.cleaned_data['color_5']

            zero_value = ['0' for x in range(int(color_4))]
            if color_4 == '8' or color_4 == '9':
                zero_value = ''

            calculation = color_1 + color_2 + color_3 + ''.join(zero_value)

            if color_4 == '-1':
                calculation = '%s%s.%s' % (color_1, color_2, color_3)
            elif color_4 == '-2':
                calculation = '%s.%s%s' % (color_1, color_2, color_3)

            if len(calculation) > 3 and color_4 != '-1' and color_4 != '-2':
                formatted = format(int(calculation), ',d')
                calculation = '.'.join(formatted.split(','))

            tolerance = color_5
            if tolerance == 'None':
                tolerance = ''
            tolerance_text = '' if tolerance == '' else '~ with tolerance +/- : %s' % tolerance

            data = {
                'calculation': calculation,
                'tolerance': tolerance,
                'colors': [
                    {'color_1': color_1},
                    {'color_2': color_2},
                    {'color_3': color_3},
                    {'color_4': color_4},
                    {'color_5': color_5}
                ],
                'plain': '%s Ohm %s' % (calculation, tolerance_text)
            }
            return HttpResponse(json.dumps(data),
                                content_type='application/json')
    else:
        form4bracelet = Resistor4BraceletsForm()
        form5bracelet = Resistor5BraceletsForm()

    context = {'form4bracelet': form4bracelet, 'form5bracelet': form5bracelet}
    return render(request, 'resistor-form.html', context)
