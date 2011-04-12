from django.utils.safestring import mark_safe
from django.forms.widgets import Select
from django.forms.util import flatatt

class ClauseSelect(Select):
    
    class Media: 
        js = ('js/clause_select.js', )
        css = {
            'screen': ('css/clause_select.css',),
        }
    
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        if 'class' in final_attrs:
            final_attrs['class'] += ' clause_select'
        else:
            final_attrs['class'] = 'clause_select'
        output = [u'<select%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append(u'</select>')
        return mark_safe(u'\n'.join(output))