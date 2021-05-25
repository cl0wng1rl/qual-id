# Qual ID - Contribution Guide

Qual ID welcomes contributions from people of all abilities. If you're new to open source software, then our issue to add data to existing categories is a _great first issue_.

If you're more experienced, or a newbie looking for something slightly more challenging, then our issue to add a new category is _perfect_.

## Add Data to an Existing Category

Adding data to a category essentially involves adding new strings to the list, `_values`, of a given category. Values must not contain any spaces or special characters, and must be appropriate to the given category. Once you've done this, simply raise a PR and it will be reviewed.

## Add a Brand New Category

Adding a new category involves adding a new class that inherits from the `Category` class. There are a few requirements for a successful PR:

- [ ] Add a new category class that inherits from `Category` class and has a `_values` list.
- [ ] Add the new category to the `All` group.

# Note

We request that for any contribution, at least 10 values are added, but of course the more the better!

There are rules in place for the code formatting. Namely, values in the list ,`_values`, must not contain special characters, spaces or upper case characters. The list must also be in alphabetical order. 

_If you see an error relating to alphabetical order, running_

```
from <YOUR_CATEGORY_FILE> import <YOUR_CATEGORY>
print(sorted(<YOUR_CATEGORY>().get_values()))
```

_will print the alphabetised list._

The formatting is done with `black`, so if you know what that means then please aim to use `black` to format your .py files.

# Thank You

Seriously, thank you for any contribution, we really appreciate it!
