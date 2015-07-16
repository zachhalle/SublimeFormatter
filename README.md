# SublimeFormatter
A Sublime Text 3 plugin which can be configured to format your code files.

# Installation
Open a shell and go to your Sublime packages directory. Clone this repository into that directory. On OS X:

    cd ~/Library/Application Support/Sublime Text 3/Packages
    git clone https://github.com/zachhalle/SublimeFormatter ./Formatter

# Configuration

Then, open your User preferences file and specify paths to formatters you'd like to use for as many file extensions
as you need. SublimeFormatter **requires** formatters which

* Support the following syntax: `path-to-formatter path-to-file`
* Output the indented code to standard output

The following configuration can be used to indent OCaml code and signature files:

    {
      ...
      "code_indent_paths": {
        ".ml": "/Users/zach/.opam/4.02.1/bin/ocp-indent",
        ".mli": "/Users/zach/.opam/4.02.1/bin/ocp-indent"
      },
      ...
    }
