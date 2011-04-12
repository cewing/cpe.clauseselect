from django.forms import ChoiceField
from django.shortcuts import render_to_response

from cpe.clauseselect.forms import SentenceForm
from cpe.clauseselect.widgets import ClauseSelect
from cpe.demoapp.models import Vehicle


class CarSelectForm(SentenceForm):

    vehicle_color = ChoiceField(
        choices=Vehicle.get_choices_for('vehicle_color', add_all=u'any color'),
        initial=u'all',
        label='all',
        widget=ClauseSelect,
        required=False)
    vehicle_type = ChoiceField(
        choices=Vehicle.get_choices_for('vehicle_type'),
        label='',
        widget=ClauseSelect)
    model_year = ChoiceField(
        choices=Vehicle.get_choices_for('model_year', add_all=u'any year'),
        initial=u'all',
        label='made in',
        widget=ClauseSelect,
        required=False)


def test_form(request):
    matches = []
    submitted = False
    if request.method == 'GET' and 'submit' in request.GET:
        submitted = True
        form = CarSelectForm(request.GET) # A form bound to the POST data
        if form.is_valid():
            form.persist_data(request.session)
            search_keys = {}
            for key in form.cleaned_data:
                if form.cleaned_data[key] != 'all':
                    search_keys[key] = form.cleaned_data[key]
            matches = Vehicle.objects.filter(**search_keys)
    else:
        form = CarSelectForm() # An unbound form
        form.initial = form.persistent_data(request.session)

    form.hide_unused_fields()
    return render_to_response('test_form.html', {
        'form': form,
        'vehicles': matches,
        'submitted': submitted,
    })
