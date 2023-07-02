# proyecto-final-fidi-db
Proyecto Final FiDi Database

## Diagrama de base de datos
```
https://app.quickdatabasediagrams.com/#/d/3G2nHC
```

## Librerias instaladas para el Backend. (contenidas en el Pipfile)
- python-dotenv
- flask-sqlalchemy
- psycopg2-binary
- flask
- flask-migrate
- flask-jwt-extended
- flask-cors

### configuracion archivo .env
  ```
  DATABASEURI="postgresql+psycopg2://postgres:postgres@localhost:5432/dbfidi"
  JWT_SECRET="f400ca7c5ef4d9dfbc31c58898cc40aa"
  ```
