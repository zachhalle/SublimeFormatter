# SublimeFormatter
A Sublime Text 3 plugin which can be configured to format your code files.

# Installation
Open a shell and go to your Sublime packages directory. Clone this repository into that directory. On OS X:

    cd ~/Library/Application Support/Sublime Text 3/Packages
    git clone https://github.com/zachhalle/SublimeFormatter ./Formatter

# Configuration

Then, open your User preferences file and specify paths to formatters you'd like to use for as many file extensions
as you need. SublimeFormatter **requires** formatters which

* Support the following syntax: `/path/to/formatter [options]`
* Receive code from standard input when called with the above syntax
* Output the indented code to standard output

Using formatters that do not adhere to this behaviour can produce undesirable results, such as erasing the contents of the current buffer (which can be undone with ctrl + Z, but still, not fun).

The following configuration can be used to indent OCaml code and signature files:

    {
      ...
      "code_format_paths": {
        ".ml": "/Users/zach/.opam/4.02.1/bin/ocp-indent",
        ".mli": "/Users/zach/.opam/4.02.1/bin/ocp-indent"
      },
      ...
    }

# Usage

SublimeFormatter can be run from the command palette. You can also create key-bindings to the command `formatter`.

![Formatter usage](http://i.imgur.com/9p3YXVc.png)

# Emphatic warning

This plugin will run commands in your shell. Measures are taken to prevent destructive input from being executed, but perhaps if you are truly enterprising you could fool the plugin. Basically, please don't attempt to use formatters or run this plugin on files whose paths attempt to hide a `rm -rf /` somewhere in there, or it might go poorly for you.
