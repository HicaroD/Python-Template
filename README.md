# Python template

My Python project configured with pre-commit, black, pylint, flake8 and etc.

## Setting up the project

1. Pre-commit

    1.1. Install `pre-commit`

    ```
    pip install pre-commit
    ```

    1.2. Add it to your `requirements.txt`

    ```
    pre-commit
    ```

    1.3. Create a `.pre-commit-config.yaml` ([example](./.pre-commit-config.yaml)) in the root directory.
    
    Just make sure all the packages used in the file updated, such as `black` and `pytest`.

    1.4. Run `pre-commit` for installing all hooks

    ```
    pre-commit install
    ```

    1.5. Now, check if everything was properly configured.

    ```
    pre-commit run --all-files
    ```
