from django import forms
from .models import Parameter, ParameterOption


class ComponentForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea())
    parameters = Parameter.objects.all()

    def __init__(self, *args, **kwargs):
        super(ComponentForm, self).__init__(*args, **kwargs)

        parameters_values = {}
        for parameter in self.parameters:
            options = ParameterOption.objects.filter(id_parameter=parameter)
            option_dict = {}
            for option in options:
                option_dict[option.name] = option.value
            parameters_values[parameter.name] = option_dict

        for parameter_name, option_dict in parameters_values.items():
            # Create a field for each parameter with choices from ParameterOption
            choices = [(value, key) for key, value in option_dict.items()]
            self.fields[parameter_name] = forms.ChoiceField(choices=choices, label=parameter_name)
