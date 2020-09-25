# Qual ID [![Qual ID](https://img.shields.io/endpoint?url=https%3A%2F%2Fqual-id.herokuapp.com%2Fbadge-endpoint%2F)](https://github.com/gabrielbarker/qual-id)

[![Heroku App Status](http://heroku-shields.herokuapp.com/qual-id)](https://qual-id.herokuapp.com)

Qual ID is a RESTful API that returns _qualitative ID's_. A _qualitative ID_ is a unique signifier that is readable and understandable to humans. This serves the same purpose as any other ID, while also being much nicer to deal with and much easier to remember.

The Qual ID can be accessed using the URL

```
https://qual-id.herokuapp.com/
```

To get Qual IDs from the REST API, supply a pattern to the `/get/` endpoint. For example:

```
https://qual-id.herokuapp.com/get/?pattern=food-animal
```

which would return a JSON object containing a Qual ID matching the `food-animal` pattern. e.g.

```json
{ "data": ["lemon-lobster"] }
```
