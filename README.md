# SublimeFormatter
A Sublime Text 3 plugin which can be configured to format your code files.

# Installation
Open a shell and go to your Sublime packages directory. Clone this repository into that directory. On OS X:

    cd ~/Library/Application Support/Sublime Text 3/Packages
    git clone https://github.com/zachhalle/SublimeFormatter ./Formatter

# Configuration

Then, open your User preferences file and specify paths to formatters you'd like to use for as many file extensions
as you need. SublimeFormatter **requires** formatters which

* Support the following syntax: `/path/to/formatter [options] /path/to/source`
* Output the indented code to standard output

The config format is as follows:

    {
      ...
      "code_indent_paths": {
        ".<file_extension_1>": "<formatter for that extension>",
        ...
        ".<file_extension_n>": "<formatter for that extension>"
      },
      ...
    }

I use the following configuration to indent OCaml code and signature files:

    {
      ...
      "code_indent_paths": {
        ".ml": "~/.opam/4.02.1/bin/ocp-indent",
        ".mli": "~/.opam/4.02.1/bin/ocp-indent"
      },
      ...
    }

I recommend using absolute paths to avoid issues with PATH variable resolving incorrectly.

# Usage

By default, SublimeFormatter is run on save. To disable this feature, add `format_on_save: False` to your global or project settings. It can be run manually from the command palette as well, or you can also create key-bindings to the command `formatter`.

![Formatter usage](http://i.imgur.com/9p3YXVc.png)

# Troubleshooting

When SublimeFormatter is run on save, if it fails it will do so silently. Run it from the command palette to view error messages.
