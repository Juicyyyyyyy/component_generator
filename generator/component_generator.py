from .open_ai.gpt import Gpt
from .open_ai.prompt import Prompt


class ComponentGenerator:
    def __init__(self, user_parameters):
        self.user_parameters = user_parameters

    def generate_component(self):
        prompt_content = Prompt.generate_component_content(self.user_parameters)
        gpt = Gpt()
        component_content = gpt.call_gpt_and_extract(prompt_content, "<component>", "</component>")
        return component_content
