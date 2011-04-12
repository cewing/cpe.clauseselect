from django import forms
# from django.utils.encoding import smart_unicode
from django.utils.safestring import mark_safe


class SentenceForm(forms.Form):
    """ a sentence form allows us to render a form as a sentence
    """
    persistable_fields = []

    def __init__(self, *args, **kwargs):
        super(SentenceForm, self).__init__(*args, **kwargs)
        if 'persistable_fields' in kwargs:
            self.persistable_fields = kwargs['persistable_fields']
        elif not self.persistable_fields:
            self.persistable_fields = self.fields.keys()
        self.label_suffix = ''

    def as_sentence(self):
        output = [u'<ul class="clause_sentence">']
        graph = self.as_ul()
        if graph:
            output.append(graph)
        output.append(u'</ul>')
        return mark_safe('\n'.join(output))

    def __unicode__(self):
        return self.as_sentence()

    def persist_data(self, session):
        """ persist data submitted in this form using the sessions framework

            for each field in self.persistable_fields, persist the data from
            self.cleaned_data IFF
                1.  cleanded_data has that key present
                2.  the value for that field in cleaned data is _not_ the same
                    as the initial value for that field (if it is the same, it
                    isn't worth persisting)
        """
        use_prefix = ['sentence', self.prefix][self.prefix is not None]
        if use_prefix not in session:
            session[use_prefix] = {}

        for field in self.persistable_fields:
            if field in self.cleaned_data:
                datum = self.cleaned_data[field]
                if datum != self.fields[field].initial:
                    session[use_prefix][field] = datum
                    session.modified = True
                else:
                    if field in session[use_prefix]:
                        del session[use_prefix][field]
                        session.modified = True

    def persistent_data(self, session):
        """ get the data persisted for this form, if any, from the session
        """
        use_prefix = ['sentence', self.prefix][self.prefix is not None]
        data = {}
        target = {}
        if use_prefix in session:
            target = session[use_prefix]
        for field in self.persistable_fields:
            if field in target:
                data[field] = target[field]

        return data

    def hide_unused_fields(self):
        """ hide any fields in the form that are not being used

            a field is not used if:
                1.  it are _not_ required, AND
                2a. the value for it is _not_ in self.data OR self.initial
                2b. the value found for it is the same as the initial value
                    for that field
        """
        for fname, field in self.fields.items():
            datum = None
            if not field.required:
                # cleaned_data contains fieldnames _without_ form prefix
                # this is !important!
                if hasattr(self, 'cleaned_data') and fname in self.cleaned_data:
                    datum = self.cleaned_data[fname]
                elif fname in self.initial:
                    datum = self.initial[fname]
                else:
                    pass
                if datum is None or datum == field.initial:
                    if 'class' in field.widget.attrs:
                        field.widget.attrs['class'] += ' refinement'
                    else:
                        field.widget.attrs['class'] = 'refinement'
