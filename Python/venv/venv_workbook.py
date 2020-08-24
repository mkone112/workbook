CREATE
    virtualenv <venv_name>
    
    python -m venv <venv_name>
    #3.3+

ACTIVATE
    Linux
        source <venv_name>/bin/activate
    Windows
        source <venv_name>/Scripts/activate.bat

DEACTIVATE
    Linux
        source <venv_name>/bin/deactivate
    Windows
        source <venv_name>/Scripts/deactivate.bat

DELETE
    just delete <venv_name> folder
    
Pipevn
#tool that aims to bring the best of ∀ packaging worlds
    bundler
    composer
    npm
    cargo
    yarn
    ...
    #to the Python world