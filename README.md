# ECS Testing

This is a repo to support a series of blog posts about testing Python code with
an entity/component/system toy engine for hands-on experimentation.

# Setup

This section should help you get the code up and running on your machine.

## Prerequisites

Before you can work with this code, please install
[poetry](https://poetry.eustace.io/docs/). I've had much better luck with the
`pip` installation process than the `get-poetry` one, if it helps.

This code also assumes that you're on 3.6+. If you don't have easy access to
it, through [(mini) Conda](https://docs.conda.io/en/latest/miniconda.html),
consider checking out [pyenv](https://github.com/pyenv/pyenv). The only tip I
have for `pyenv` is to be careful in what order you put it in your `rc` file,
as it can interfere with the `poetry` virtual environment if it takes
precedence. 

### Assumptions

Some basic assumptions:

* You can read Python
* You have a text editor that you're fluent with
* You can get the prerequisites installed
* You understand `git` well enough to clone this repo to your local machine
