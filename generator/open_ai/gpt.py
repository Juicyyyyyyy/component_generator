from openai import OpenAI
from decouple import config
import re


class Gpt:

	def call_gpt(self, prompt):
		# Initialize OpenAI API with the key from the environment
		client = OpenAI(api_key=config("OPENAI_API_KEY"),)

		# Process the prompt and return the result
		response = client.chat.completions.create(
			model="gpt-3.5-turbo",
			messages=[
				{"role": "user", "content": prompt},
			]
		)
		print(response)
		print(response.choices[0].message.content)
		return response.choices[0].message.content

	def extract_text_between_tags(self, text, start_tag, end_tag):
		pattern = re.escape(start_tag) + r"(.*?)" + re.escape(end_tag)
		matches = re.findall(pattern, text, re.DOTALL)
		return matches[0].strip() if matches else ""

	def call_gpt_and_extract(self, prompt, start_tag, end_tag):
		response = self.call_gpt(prompt)
		extracted_response = self.extract_text_between_tags(response, start_tag, end_tag)
		return extracted_response
