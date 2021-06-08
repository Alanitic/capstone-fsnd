# Capstone FSND

## Table of Contents

1. [Motivation](#Motivation)
2. [About](#About)
3. [Dependencies](#Dependencies)
4. [Running](#Running)
5. [Deployed app](#Deployed-app)
6. [Roles and permissions](#Roles-and-permissions)
7. [Endpoints](#Endpoints)
8. [Examples](#Examples)
9. [ExamTestingples](#Testing)

## Motivation

This project is part of [Full stack web developer nanodegree program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044), a really challenge but full of learn program with all needed to succeed as a Full Stack Web Developer.

## About

This project allows to Create, Read, Update and Delete (CRUD) movies actors and the roles between both using Role Based Control Access (RBCA) with Auth0 as the third party authentication system.

## Dependencies

Install dependencies

```console
$ pip3 install requirements.txt
```

## Running

Start server

```console
$ export FLASK_APP=app.py
```

Enable debug mode

```console
$ export FLASK_ENV=development
```

Also, the following vairables are needed to run properly

```console
$ export AUTH0_DOMAIN='your_auth0_domain'
$ export ALGORITHMS='["algorithm_to_use"]'
$ export API_AUDIENCE='your_api_audience'
$ export DB_URL='postgresql://<db_user>:<db_psw>@<db_url>:<db_port>/<db_to_connect>'
```

## Deployed app

A deployed and functional version can be visited [here](http://capstonefsnd-env.eba-mhvshfmh.us-east-2.elasticbeanstalk.com/).

## Roles and permissions

The following roles are taking into account

- Casting Assistant
  - Can view actors and movies
- Casting Director
  - All permissions a Casting Assistant has and…
  - Add or delete an actor from the database
  - Modify actors or movies
- Executive Producer
  - All permissions a Casting Director has and…
  - Add or delete a movie from the database

## Endpoints

| Method | Endpoint          | Description                                | Arguments            |
| ------ | ----------------- | ------------------------------------------ | -------------------- |
| GET    | /actors           | Fetches all existing actors as JSON format | None                 |
| GET    | /movies           | Fetches all existing movies as JSON format | None                 |
| POST   | /actors           | Creates a new movie                        | title, release_date  |
| POST   | /movies           | Creates a new actor                        | name, age and gender |
| PATCH  | /actor/<actor_id> | Updates an existing actor                  | name, age, gender    |
| PATCH  | /movie/<movie_id> | Updates an exising movie                   | title, release_date  |
| DELETE | /actor/<actor_id> | Deletes an existing actor                  | None                 |
| DELETE | /movie/<movie_id> | Deletes an existing movie                  | None                 |

## Examples

### GET /actors

Response

```json
{
  "actors": [
    {
      "age": 25,
      "gender": "Male",
      "id": 1,
      "name": "Example"
    }
  ]
}
```

### GET /movies

Response

```json
{
  "movies": [
    {
      "id": 1,
      "releaseDate": "Wed, 26 May 2021 17:34:17 GMT",
      "title": "Just an example"
    }
  ]
}
```

### POST /actors

Body

```json
{
  "name": "Example",
  "age": 25,
  "gender": "Male"
}
```

Response

```json
{
  "success": true
}
```

### POST /movies

Body

```json
{
  "title": "Just an example",
  "release_date": "2021-05-26 11:34:17"
}
```

Response

```json
{
  "success": true
}
```

### PATCH /actor/int:id

Body

```json
{
  "name": "Exmaple 2",
  "age": 25,
  "gender": "Male"
}
```

Response

```json
{
  "actor": {
    "age": 25,
    "gender": "Male",
    "id": 1,
    "name": "Exmaple 2"
  },
  "success": true
}
```

### PATCH /movie/int:id

Body

```json
{
  "title": "Flaskman"
}
```

Response

```json
{
  "movie": {
    "id": 1,
    "releaseDate": "Wed, 26 May 2021 17:34:17 GMT",
    "title": "Flaskman"
  },
  "success": true
}
```

### DELETE /actor/int:id

Response

```json
{
  "actor": {
    "age": 25,
    "gender": "Male",
    "id": 1,
    "name": "Exmaple 2"
  },
  "success": true
}
```

### DELETE /movie/int:id

Response

```json
{
  "actor": {
    "id": 1,
    "releaseDate": "Wed, 26 May 2021 17:34:17 GMT",
    "title": "Flaskman"
  },
  "success": true
}
```

## Testing

The testing file `postman-test.json` should be imported from postman and run all needed tests.
