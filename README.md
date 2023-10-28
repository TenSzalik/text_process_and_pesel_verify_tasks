# Contelizer recruitment task

A Django website with two services: one for checking the PESEL* number and extracting information from it (gender and date of birth). The other service is for uploading .txt files and shuffling the letters in each word.

*PESEL is the national identification number used in Poland since 1979. It always has 11 digits, identifies just one person and cannot be changed to another one.

## How to run

1. Install docker and docker compose

2. Go to the `contelizer_task/`

3. Run: `docker compose up -- build`

Now you can go to the home page `http://0.0.0.0:8000/` and send forms.

## Useful commands

1. Linter:

    `docker exec -it <container_name> ruff check .`

2. Formatter

    `docker exec -it <container_name> black .`

3. Testing

    `docker exec -it <container_name> pytest`

## Acknowledgements

The project was done according to the requirements specified during the recruitment of Contelizer Junior Python Developer. Thanks! It was a fun project.