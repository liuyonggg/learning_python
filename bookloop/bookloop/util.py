class Fieldset(object):
    def __init__(self, form, name=None, readonly_fields=(), fields=(), classes=(),
      description=None, model=None):
        self.form = form
        self.name, self.fields = name, fields
        self.classes = ' '.join(classes)
        self.description = description
        self.model= model
        self.readonly_fields = readonly_fields

    def _media(self):
        return None
    media = property(_media)

    def __iter__(self):
        for field in self.fields:
            yield Fieldline(self.form, field, self.readonly_fields, model=self.model)

class Fieldline(object):
    def __init__(self, form, field, readonly_fields=None, model=None):
        self.form = form  # A django.forms.Form instance
        if not hasattr(field, "__iter__") or isinstance(field, six.text_type):
            self.fields = [field]
        else:
            self.fields = field
        self.has_visible_field = not all(field in self.form.fields and
                                         self.form.fields[field].widget.is_hidden
                                         for field in self.fields)
        self.model= model
        if readonly_fields is None:
            readonly_fields = ()
        self.readonly_fields = readonly_fields

    def __iter__(self):
        for i, field in enumerate(self.fields):
            yield Field(self.form, field, is_first=(i == 0))

    def errors(self):
        return mark_safe(
            '\n'.join(self.form[f].errors.as_ul()
            for f in self.fields if f not in self.readonly_fields).strip('\n')
        )

class Field(object):
    def __init__(self, form, field, is_first):
        self.field = form[field]  # A django.forms.BoundField instance
        self.is_first = is_first  # Whether this field is first on the line
        self.is_checkbox = isinstance(self.field.field.widget, forms.CheckboxInput)
        self.is_readonly = False

    def label_tag(self):
        classes = []
        contents = conditional_escape(force_text(self.field.label))
        if self.is_checkbox:
            classes.append('vCheckboxLabel')

        if self.field.field.required:
            classes.append('required')
        if not self.is_first:
            classes.append('inline')
        attrs = {'class': ' '.join(classes)} if classes else {}
        # checkboxes should not have a label suffix as the checkbox appears
        # to the left of the label.
        return self.field.label_tag(contents=mark_safe(contents), attrs=attrs,
                                    label_suffix='' if self.is_checkbox else None)

    def errors(self):
        return mark_safe(self.field.errors.as_ul())

