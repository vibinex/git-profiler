from ruamel.yaml import YAML
import os

class LanguageExtractor():
	def __init__(self):
		self.lang_map = self.get_language_map()

	def get_language_map(self):
		yaml=YAML(typ='safe')
		with open("../languages.yml") as f:
			lang_map = f.read()
		lang_map = yaml.load(lang_map)
		return lang_map

	def get_language_from_file(self, filename):
		_, file_extension = os.path.splitext(filename)
		fn_options = []
		ext_options = []
		for key in self.lang_map.keys():
			if 'extensions' in self.lang_map[key].keys():
				if file_extension in self.lang_map[key]['extensions']:
					ext_options.append(key)
			elif 'filenames' in self.lang_map[key].keys():
				if filename in self.lang_map[key]['filenames']:
					fn_options.append(key)
			else:
				# print(key, self.lang_map[key])
				pass

		if len(fn_options) == 1:
			return fn_options[0]
		elif len(fn_options) == 0:
			if len(ext_options) == 1:
				return ext_options[0]
			elif len(ext_options) == 0:
				print("Warning: No languages found for file '"+filename+"'")
				return None
			else:
				print("Warning: Multiple languages found for file '"+filename+"': ", ext_options)
				return ext_options[0]
		else:
			print("Warning: Multiple languages found for file '"+filename+"': ", fn_options)
			return fn_options[0]

if __name__ == '__main__':
	le = LanguageExtractor()
	print(le.get_language_from_file("test.py"))
	print(le.get_language_from_file('sshconfig.snip'))