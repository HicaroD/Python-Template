# Python template

My Python project configured with pre-commit, black, pylint, flake8 and etc.

## Setting up the project

0. Create a virtual environment (using `venv`, `conda` or any package you want)

1. `pylint`

    1.1. Install `pylint` in your virtual environment

    ```
    pip install pylint
    ```

    1.2. Create a `.pylintrc` (see an example [here](./.pylintrc))

2. `black`

    2.1. Install `black` in virtual environment

    ```
    pip install black
    ```

3. `pre-commit`

    3.1. Install `pre-commit` in your virtual environment

    ```
    pip install pre-commit
    ```

    3.2. Add it to your `requirements.txt`

    ```
    pre-commit
    ```

    3.3. Create a `.pre-commit-config.yaml` ([example](./.pre-commit-config.yaml)) in the root directory.
    
    Just make sure all the packages used in the file updated, such as `black` and `pytest`. In this
    file, at the end you have an instruction for automating the creation of `requirements.txt`,
    and it uses the name of your virtual environment, make sure the name of your virtual
    environment matches the name used in the pre-commit configuration.

    3.4. Run `pre-commit` for installing all hooks

    ```
    pre-commit install
    ```

    3.5. Now, check if everything was properly configured.

    ```
    pre-commit run --all-files
    ```

