# avt12-template

-requirements.txt
-MAKEFILE
-github actions
-devcontainer


#[![CI](https://github.com/nogibjj/avt12-template/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/avt12-template/actions/workflows/hello.yml)

The repository serves as a python template. Below, the actions comprising the workflow run are explained- these are articulated in the yml file as instructions to build:

**Setup actions ** involves getting ready for the job. This is followed by **checkout@v3**, which refers to the runner accessing and cloning the codebase within the repository to perform actions. 

**Setup Python 3.8** refers to the version of Python to install on the runner to execute the actions.

**Install packages** refers to the installation of the packages and their respective versions as per the "requirements.txt" file. 

**Lint** automatically analyzes the code to detect for errors or improper stylistic coding. In this case, the code was rated at 10/10.
<img width="707" alt="lint" src="https://github.com/user-attachments/assets/e3880e20-ad19-4340-98f5-e615b4c31b5d">

**Test** refers to the process of automatically running tests to ensure that the code works as part of the continuous integration concept.
<img width="479" alt="test" src="https://github.com/user-attachments/assets/4569badb-516c-4733-b990-86b788e016bc">

**Format** refers to the appropriate styling and indentation as part of the code. The "black.py" refers to ensuring that the code is within a particular style guide.

There are finally post-run actions like logistic metrics, report preparation, or removing temporary folders, before the build is complete.

The included files comprising the template all serve important purposes:
**Main.py** refers to the primary function to be conducted as part of the program. This is tested in "**test_main.py**", where the function is given validating answers to ensure that the program can catch errors accompanying changes.

The **dockerfile** serves to include the packages necessary to run the code, automates the runtime environment, and ensures a consistent practice across machines and programs. The **devcontainer** serves a similar purpose to ensure the same environment is used to run the code.

The **makefile** serves to provide instructions on what to compile within the program, and automate building. In the install line, the versions of the programs specified in the "requirements.txt" file are installed.

The **gitignore** file ensures that unnecessary files remain untracked and are not pushed.
