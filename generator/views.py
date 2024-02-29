from django.shortcuts import render
from .models import Project, Component, Parameter, ParameterOption
from .forms import ComponentForm
from .component_generator import ComponentGenerator


def generate_component(request):
    component_has_been_generated = False
    component_content = ''
    if request.method == 'POST':
        print(request)
        form = ComponentForm(request.POST)
        if not form.is_valid():
            print("Form errors:", form.errors)

        if form.is_valid():
            description = form.cleaned_data['description']
            type_of_component = form.cleaned_data['type of component']
            language = form.cleaned_data['language']
            color_palette = form.cleaned_data['color palette']
            font_style = form.cleaned_data['font style']
            user_parameters = {'description': description, 'type_of_component': type_of_component, 'language': language,
                               'color_palette': color_palette, 'font_style': font_style}

            project = Project.objects.create(
                owner_id=request.user,
                description=description,
                type_of_section=type_of_component,
                language=language,
                color_palette=color_palette,
                font_style=font_style
            )
            project.save()

            component_generator = ComponentGenerator(user_parameters)
            component_content = component_generator.generate_component()

            component = Component.objects.create(code=component_content, project_id=project)
            component.save()

            component_has_been_generated = True
    else:
        form = ComponentForm()

    parameters = Parameter.objects.all().order_by('order')
    parameter_options = ParameterOption.objects.all()
    return render(request, 'software/generate_component.html', {'parameters': parameters,
                                                                'parameter_options': parameter_options, 'form': form,
                                                                'component_has_been_generated': component_has_been_generated,
                                                                'component_content': component_content})
