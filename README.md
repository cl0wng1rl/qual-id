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
  <a href="https://qual-id.herokuapp.com/get/?categories=fruit-geography">
    <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fqual-id.herokuapp.com%2Fbadge-endpoint%2F"/>
  </a>
  <a href="https://github.com/psf/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg" />
  </a>
  <a href="https://hacktoberfest.digitalocean.com/">
    <img src="https://img.shields.io/badge/Hacktoberfest-2020-blueviolet" />
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" />
  </a>

<b>A RESTful API that returns randomly generated, custom _qualitative ID's_</b>

<a href="#using-the-api">Using the API</a> •
<a href="#using-the-cli">Using the CLI</a> •
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

### The 'get' Endpoint

#### **The `categories` Parameter**

To get Qual IDs from the REST API, supply categories, separated by hyphens, to the `/get/` endpoint. For example:

```
https://qual-id.herokuapp.com/get/?categories=food-animal
```

which would give a JSON object, with results in the form of a _food_ followed by an _animal_. e.g.

```json
{ "data": ["lemon-lobster"] }
```
In addition to defined categories, the word `random` can be used, which will use a random category in it's place.

#### **The `number` Parameter**

As well as the `categories` parameter, the `number` parameter can also be used, to determine how many Qual ID's will be returned. For example:

```
https://qual-id.herokuapp.com/get/?categories=food-animal&number=3
```

which would return a JSON object containing 3 Qual ID's matching the `food-animal` pattern. e.g.


```json
{ "data": ["lemon-lobster", "cookie-whale", "egg-lizard"] }
```

#### **The `format` Parameter**

The `format` parameter can also be used to determine in what format the results will be returned. This value is, by default, _"json"_, but can also be _"csv"_, which gives results in simple comma-separated format. e.g.

```
https://qual-id.herokuapp.com/get/?categories=food-animal&format=csv
```
which would return

```js
"lemon-lobster"
```

#### **The `group` Parameter**

By default, all categories are avaiable, but if you want a more predictable range of categories when using `random`, you can supply a `group`. A group is a subset of all the categories, and `random` will only return a category from this group. Examples of groups are _"all"_ (which is the default group), _"minimal"_ and _"neutral"_. e.g.

```
https://qual-id.herokuapp.com/get/?categories=food-random&group=minimal
```

### The 'categories' Endpoint

The `/categories/` endpoint returns a list of categories that can are accepted by the 'get' endpoint. For example:

```
https://qual-id.herokuapp.com/categories/
```

would return a JSON object containing the list of category names, e.g.

```json
{ "data": ["animal", "food", ...] }
```

The 'categories' endpoint also accepts a `group` paramter.

## Using The CLI

The Qual ID CLI allows qual ID's to be generated locally. It only requires `python3` to be installed.

### Installation

To use the Qual ID CLI, run
```bash
curl -s "https://raw.githubusercontent.com/gabrielbarker/qual-id/main/bin/install.sh"|sh -s <INSTALL_DIRECTORY>
```
where `<INSTALL_DIRECTORY>` is the path of a directory that is part of your terminal path. _Note: If omitted, the current directory is used_

Or alternatively, download the [latest release](https://github.com/gabrielbarker/qual-id/releases/latest) tar file. Then unzip, and place the `qual_id` directory and `qid` executable in a directory that is part of your terminal path.

### qid

To view the help for `qid`, run

```bash
qid --help
```

This will give you the basics, but what follows is a more detailed description of some of `qid`'s features.

#### **Generating Qual ID's**

To generate a qual ID, run

```bash
qid --categories flower bread
```

where "flower" and "bread" can be replaced by the names of up to 5 categories. The above command will return, for example,

```bash
poppy-pumpernickel
```
_Note: the CLI has 'csv' format by default._

The same parameters available in the REST API are available in the CLI. The following is an example of a command using all possible options:

```bash
qid --categories flower cake --group neutral --format json --number 3
```

or with shortened flags:

```bash
qid -c flower cake -g neutral -f json -n 3
```
returning, for example,

```json
{"data": ["chrysanthemum-crumpet", "wisteria-tart", "saffron-panettone"]}
```

#### **Info**

Unique to the CLI is the _info_ subcommand. _info_ allows you to see possible options for all parameters, and what values are contained in a given category.

To see a list of all categories, run 

```bash
qid info --category
```

To see a list of all groups, run 

```bash
qid info --group
```

To see a list of all categories in a given group, run 

```bash
qid info --group minimal
```
_where minimal can be any group name._

To see a list of all values for a given category, run 

```bash
qid info --category animal
```
_where animal can be any category name._

To see a list of all available formats, run 

```bash
qid info --format
```


# Contributing

This repo strongly welcomes all contributions! Whether to documentation, assets, data, or code. There are standing issues to add values to existing categories, or add new categories all together. You can see the full contribution guide [here.](./CONTRIBUTING.md)

# License

[MIT](./LICENSE)
