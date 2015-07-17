import sublime, sublime_plugin
import subprocess

class FormatterCommand(sublime_plugin.TextCommand):
	
	def get_extension(self, fname):
		idx = fname.rfind('.')
		return fname[idx:]
		

	def run(self, edit):
		
		fname = self.view.file_name()

		if not self.view.settings().has('code_format_paths'):
			sublime.error_message('Formatter needs the code_indent_paths setting to be configured.')
			return

		extension = self.get_extension(fname)
		indent_paths = self.view.settings().get('code_format_paths')

		if not extension in indent_paths:
			sublime.error_message('Formatter does not have an indenter configured for the extension ' + extension)
			return



		indent_path = indent_paths[extension]
		content = sublime.Region(0, self.view.size())

		try:
			cmd_string = 'path fname'.replace('path', indent_path).replace('fname', fname)
			indented = subprocess.check_output(cmd_string, shell=True)
			self.view.replace(edit, content, "".join(map(chr, indented)))
		except subprocess.CalledProcessError as e:
			sublime.error_message('Error while running indenter:'.replace(e.output))