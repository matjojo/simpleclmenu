# SimpleCLMenu
A simple commandline menu utility for your python3 menu needs.

## Installation
`pip install simpleclmenu`

##Syntax
```python
get_choice_from_cli([
("index", "displayed option", "default returned value"),
])
```
##Simple Usage
This code:
```python
from simpleclmenu import get_choice_from_cli

choice = get_choice_from_cli([
(1, "Run as Client", client_run),
(2, "Run as Server", server_run),
('q', "Quit", sys.exit),
])

choice()
```
Will show this output:
```
Select one option from the list:
1	Run as Client
2	Run as Server
q	Quit
Selection > q

Process finished with exit code 0
```
##Advanced options
#### Default options:
```python
choice = get_choice_from_cli(options,
                        repeat_until_correct=True,
                        return_key=False,
                        title="Select one option from the list:",
                        prompt="Selection > ",
                        redo_text="Not a valid selection, try again.")
```
#### Options
- options: A list of options, which are three item tuples with [0]=index, [1]=description/name, [2]=object  
    0.The index needs to be convertible to string and printable.  
    1.The description/name needs to be printable.  
    2.The object doesn't have any requirements on it's type.  
- repeat_until_correct: If True: keeps checking until valid option is selected.  
    - If False: faulty option key is returned regardless of value of return_key.
- return_key: If True the index for the selected option is returned instead of the third item in the tuple.
- title: The title shown above the option list. (Pass None for no title)
- prompt: The prompt shown below the options list. (Pass None for no prompt(just a new line))
- redo_text: The text shown when a invalid option is chosen and return_until_correct is set (pass None for no redo text)
- returns: The callback that is chosen, or the given key if return_key is set


























