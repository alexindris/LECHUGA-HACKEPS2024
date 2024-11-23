# Install Devbox shell

https://www.jetify.com/docs/devbox/installing_devbox/?install-method=wsl

task deps
task dev

python manage.py migrate
python manage.py runserver

# Playground of enpoints

http://127.0.0.1:8000/graphql
Or use postman --> http://127.0.0.1:8000/graphql/

lsof -i :8000
kill -9 xxxx

# Pending

- CodeQL
- Dependabot
- CI ?

- CreateUser
- Login User (DONE)
- Store (DONE)
- Authentication on FE

# Update graphQL endpoints in FE

execute pnpm codegen --watch
Recomended extension for GraphQL:

- GraphQL: Syntax Highlighting

Also to work with

# Using apollo client

You have to open in a terminal "pnpm codegen --watch" while you create the query
If you don't do that, the VSC editor will not recognize the query and it will show as "unknown"

All the queries are in api.tsx file.
IMPORTANT TO BE TSX. IF NOT, SHIT HAPPENS.

# New py endpoint

1. main_app/accounts/new_test.py
2. Create the test there
3. Create the necesari things, probably in the actions.py file
4. TDD
