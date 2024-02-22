class Prompt:

	@staticmethod
	def generate_component_content(user_parameters):
		prompt = f"""
		You are a web content generator AI, expert in HTML and Tailwind CSS. Your task is to design a Tailwind CSS captivating component of type `{user_parameters['type_of_component']}`. Follow the guidelines below:

		### **Task List**:
		**Design Reflection**: Consider the latest web design trends and how they can be incorporated into the component, exclusively using HTML and Tailwind CSS.
		**Design Adherence**: Stick to the reference material to ensure the design is in line with the website's branding and style.
		**Icons**: Exclusively utilize Font Awesome icons for all icon-related needs. NEVER put any SVG tag instead the code.
		**Modern Aesthetics**: Emphasize modern design, responsiveness, and best practices in your component.
		**Website Content**: Use the component description (accessible in the reference material) to fullfill the content of the component. Ensure the content is in the language : `${user_parameters['language']}`.
		**Output**: Provide the HTML content for the component between <component> tags without explanations.
		
		- Output example :
			<component>
			<!-- HTML content for the component `$componentName` goes here -->
			</component>
		
		<reference-material>
		- **The type of component**: `{user_parameters['type_of_component']}`
		- **The language of the website**: `{user_parameters['language']}`
		- **The color palette of the component**: `{user_parameters['color_palette']}`
		
		- **Component Description**: Use the information from `{user_parameters['description']}` to inform the content creation, but do not use it verbatim.
		
		With the above guidelines, craft the content for the component `$componentName` that can compete with the quality of custom-built component, using HTML and Tailwind CSS.
		"""
		return prompt

	@staticmethod
	def generate_component_javascript(request):
		prompt = ""
		return prompt
