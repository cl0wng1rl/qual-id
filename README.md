<div align="center">
<h1>Qual ID</h1>
  <a href="https://travis-ci.com/gabrielbarker/qual-id">
    <img src="https://travis-ci.com/gabrielbarker/qual-id.svg?branch=main"/>
  </a>
  <a href="https://codecov.io/gh/gabrielbarker/qual-id">
    <img src="https://codecov.io/gh/gabrielbarker/qual-id/branch/main/graph/badge.svg"/>
  </a>
  <a href="https://qual-id.herokuapp.com">
    <img src="http://heroku-shields.herokuapp.com/qual-id"/>
  </a>
  <a href="https://qual-id.herokuapp.com/get/?pattern=food-animal">
    <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fqual-id.herokuapp.com%2Fbadge-endpoint%2F"/>
  </a>
  <a href="https://hacktoberfest.digitalocean.com/">
    <img src="https://img.shields.io/badge/Hacktoberfest-2020-blueviolet" />
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" />
  </a>

<b>A RESTful API that returns randomly generated, custom _qualitative ID's_</b>

<a href="#using-the-api">Using The API</a> •
<a href="#contributing">Contributing</a> •
<a href="#license">License</a>

</div>
<br>

Qual ID is a RESTful API that returns _qualitative ID's_. A _qualitative ID_ is a unique signifier that is readable and understandable to humans. This serves the same purpose as any other ID, while also being much nicer to deal with and much easier to remember.

## Using The API

The Qual ID REST API can be accessed using the URL

```
https://qual-id.herokuapp.com/
```

### The 'categories' Endpoint

The 'categories' endpoint returns a list of categories that can be composed to make _patterns_ accepted by the 'get' endpoint. For example:

```
https://qual-id.herokuapp.com/categories/
```

which would return a JSON object containing the list of category names, e.g.

```json
{ "data": ["animal", "food"] }
```

### Qual ID Patterns

An acceptable pattern for the 'get' endpoint is any list of up to 5 categories, joined by hyphens. For example,

```
food-animal
```

which would give results in the form of a _food_ followed by an _animal_. In addition categories, the word `random` can be used, which will use a random category in it's place.

### The 'get' Endpoint

To get Qual IDs from the REST API, supply a pattern to the `/get/` endpoint. For example:

```
https://qual-id.herokuapp.com/get/?pattern=food-animal
```

which would return a JSON object containing a Qual ID matching the `food-animal` pattern. e.g.

```json
{ "data": ["lemon-lobster"] }
```

In addition to the `pattern` parameter, the `number` parameter can also be used, to determine how many Qual ID's matching a given pattern will return. For example:

```
https://qual-id.herokuapp.com/get/?pattern=food-animal&number=3
```

which would return a JSON object containing a Qual ID matching the `food-animal` pattern. e.g.

```json
{ "data": ["lemon-lobster", "cookie-whale", "egg-lizard"] }
```

# Contributing

This repo strongly welcomes all contributions! Whether to documentation, assets, data, or code. There are standing issues to add values to existing categories, or add new categories all together. You can see the full contribution guide [here.](./CONTRIBUTING.md)

# License

[MIT](./LICENSE)
