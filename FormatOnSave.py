import sublime, sublime_plugin

class FormatOnSave(sublime_plugin.EventListener):
    def on_pre_save(self, view):

        global_settings = sublime.load_settings(self.__class__.__name__+'.sublime-settings')
        should_run = view.settings().get('format_on_save', global_settings.get('format_on_save', True))

        if not should_run:
            return

        view.run_command('formatter', {'verbose': False})
