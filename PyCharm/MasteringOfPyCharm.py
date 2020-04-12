change fonts

The layout -> The minimalist
Style hierarchies
TextMate bundles
Go to definition or navigate to declaration
Swithcer tool
Project panel
Structure panel
ace jump
collecting runtime types
adding type information
doc_mode
The lens mode
diagrams
method hierarhies
creating virtualenvs
through the terminal
using Vagrant in PyCharm
The PyCharm Console
#pycharm provide code completion inside the console
Dealing with threads and processes
  Debugging from the console
    Attach to Process
Profiling
IntelliJ ecosystem
YouTrack.JetBrains
What makes a good plugin
File Templates & Snippets(fragment)
Snippets
#live templates
Surround templates
JS support
  Getting the most out of JS code completion
    JSDoc
    libraries
  Transpiled to JS
  Support lib & frameworks
    client-side
    Server-side(& NodeJS)
  JS code quality tools
HTML & CSS
  Emmet
  Live debugging
    installing plugin
  file watchers
WEB DEVELOPMENT
  db tools
    adding a data source
      connecting to a db
      adding files
    sql console
      parameterized statements
      console history
      database diagrams
    exporting data
      copying DDLs
      exporting the table contents
  web frameworks
    common features
      support for templating engines
      customizing project creation
      debugging in templates
    DJANGO
      model dependency diagrams
      Manage.py tasks
      Django Console
mako - templating languages
file->setting->appearance&behavior->keymap

The Code Completion feature lets you quickly complete different kinds of statement in the code. Start typing object name and press CTRL+SPACE TO COMPLETE IT

A special variant of the Code Completion feature invoked by pressing CTRL-SPACE twice allows you to complete the name of any class no matter if it was imported in the current file or not. If the class not imported yet, the import statement is generated automatically

find all places where a particular obj is used in the whole project by positioning the caret at the symbol's name or at its usage in code and pressing ALT-F7(find usages in the popup menu)
view->quick documentation ~ CTRL-Q

to navigate to the declaration of a obj used somewhere in the code, position the caret at the usage and press CTRL-B or I can also click the mouse on usages with the CTRL key pressed to jump to declaration

quickly navigate in the currently edites file with CTRL-F12(NAVIGATE->File Structure) it shows the list of members of the current class.Select an element you want to navigate to and press ENTER or F4, to easyly locate an item in the list just start typing its name
rename local var of all places where they are used, place caret at the var, and press Sh-f6(refactor|rename)

When using Code Completion,accept the currently selection with Tab key,Unlike accepting with Enter,the selected name will overwrite the rest of the name to the right of the caret

SHIFT-Click or MiddleButtonMouse to close tab/tool window under the mouse cursor

Alt-F1 - select the currently edited element(class/method/field) in any view(project/structure/etc)

The speed search is available in all the tree view:start typing and you'll quickly locate the necessary item

ESC in tools windows moves the focus to the editor

SH+Escape moves the focus to the editor and also hides the current/last active tool window

F12 moves the focus from the editor to the last focused tool window

CTRL-W or Dblclk  extend selection in the editor selects the word at the caret and expanding areas of source code(For example:select method->expression that calls him->whole statement->code block->etc)

IPYTHON NOTEBOOK
  pip install ipython[all]
