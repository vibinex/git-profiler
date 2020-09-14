from ruamel.yaml import YAML
import os

def get_language_map():
	yaml=YAML(typ='safe')
	with open("../languages.yml") as f:
		lang_map = f.read()
	lang_map = yaml.load(lang_map)
	return lang_map

def get_language_from_file(filename):
	_, file_extension = os.path.splitext(filename)
	lang_map = get_language_map()
	fn_options = []
	ext_options = []
	for key in lang_map.keys():
		if 'extensions' in lang_map[key].keys():
			if file_extension in lang_map[key]['extensions']:
				ext_options.append(key)
		elif 'filenames' in lang_map[key].keys():
			if filename in lang_map[key]['filenames']:
				fn_options.append(key)
		else:
			# print(key, lang_map[key])
			pass

	if len(fn_options) == 1:
		return fn_options[0]
	elif len(fn_options) == 0:
		if len(ext_options) == 1:
			return ext_options[0]
		elif len(ext_options) == 0:
			return None
		else:
			print("Warning: Multiple languages found for file '"+filename+"': ", ext_options)
			return ext_options[0]
	else:
		print("Warning: Multiple languages found for file '"+filename+"': ", fn_options)
		return fn_options[0]

if __name__ == '__main__':
	print(get_language_from_file("test.py"))
	print(get_language_from_file('sshconfig.snip'))