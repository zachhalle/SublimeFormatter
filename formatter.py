import sublime, sublime_plugin
import subprocess
import os.path

class FormatterCommand(sublime_plugin.TextCommand):
	
	def get_extension(self, fname):
		idx = fname.rfind('.')
		return fname[idx:]
		

	def run(self, edit, **kwargs):
		
		fname = self.view.file_name()
		settings = self.view.settings()
		verbose = True if not 'verbose' in kwargs else kwargs['verbose']

		if not settings.has('code_format_paths'):
			if verbose:
				sublime.error_message('Formatter needs the code_format_paths setting to be configured.')
			return

		extension = self.get_extension(fname)
		indent_paths = settings.get('code_format_paths')

		if not extension in indent_paths:
			if verbose:
				sublime.error_message('Formatter is not configured for the extension ' + extension)
			return

		indent_path = indent_paths[extension]
		exe = indent_path.split(' ')[0]
		if not os.path.exists(exe):
			if verbose:
				sublime.error_message('Formatter is not a valid path name: ' + exe)
			return

		content = sublime.Region(0, self.view.size())

		try:
			cmd_string = 'echo "code" | path'.replace('path', indent_path).replace('code', self.view.substr(content))
			indented = subprocess.check_output(cmd_string, shell=True)
			self.view.replace(edit, content, "".join(map(chr, indented)))
		except subprocess.CalledProcessError as e:
			sublime.error_message('Error while running indenter: ' + e.output)

class FormatOnSave(sublime_plugin.EventListener):
    
    def on_pre_save(self, view):

        global_settings = sublime.load_settings(self.__class__.__name__+'.sublime-settings')
        should_run = view.settings().get('format_on_save', global_settings.get('format_on_save', True))

        if not should_run:
            return

        view.run_command('formatter', {'verbose': False})
