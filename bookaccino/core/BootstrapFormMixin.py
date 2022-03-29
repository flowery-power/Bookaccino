# class BootstrapFormMixin:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._init_bootstrap_fields()
#
#     def _init_bootstrap_fields(self):
#         for (_, field) in self.fields.items():
#             if 'class' not in field.widget.attrs:
#                 field.widget.attrs['class'] = ''
#             field.widget.attrs['class'] += ' form-control input__item'

class BootstrapFormViewMixin:
    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        self.__apply_bootstrap_classes(form)
        return form

    def __apply_bootstrap_classes(self, form):
        for (_, field) in form.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
            }
