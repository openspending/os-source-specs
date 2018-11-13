# OpenSpending Source Specs

[![Gitter](https://img.shields.io/gitter/room/openspending/chat.svg)](https://gitter.im/openspending/chat)
[![Travis](https://img.shields.io/travis/openspending/os-source-specs.svg)](https://travis-ci.org/openspending/os-source-specs)

This repository contains `fiscal.source-spec.yaml` files for use by [`os-data-importers`](https://github.com/openspending/os-data-importers), to automate the uploading of fiscal data to [OpenSpending](https://openspending.org/).

## How can I contribute fiscal specs?

To update or add new specs, fork this repository, and create a directory for your country within the appropriate top-level directory, then add a valid `fiscal.source-spec.yaml` file. The fiscal spec file defines data sources and processing steps for use by [`os-data-importers`](https://github.com/openspending/os-data-importers) to download, process, and create a fiscal datapackage for OpenSpending.

Please submit changes via a Pull Request to this repository. All `fiscal.source-spec.yaml` files must validate against the `schema.json` json-schema file before they can be merged.

You can test your fiscal spec by creating a Pull Request, or locally with the node application [pajv](https://github.com/json-schema-everywhere/pajv):

```sh
$ npm install -g pajv
$ pajv -s schema.json -d "<continent>/<country>/fiscal.source-spec.yaml"
```
