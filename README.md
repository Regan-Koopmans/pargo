# Pargo
## The Python Project Manager :snake:

This is a small tool I made for creating and managing Python projects, after being inspired by Rust's fantastic tool Cargo for project management.

To use this command, create a bash script (or a .bat file for the Windows people), and invoke `python pargo` while parsing arguments. I may include examples in the future. :wink:

## Commands supported

All commands are run using the patter `pargo [command]`

- `new` - creates a new project via cli wizard.
- `run` - will run the Python file specified as the entry-point to the program.
- `test` - will run the Python file file associated with testing.

## .pargo.json

All project data is kept in the .pargo.json file, which is generated when the user creates a new project.

## Ideas for future work

- Actually implementing a proper test framework.
- Allowing for custom linting (`pargo check-src`?)
