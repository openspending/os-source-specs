# OpenSpending Source Specs

[![Gitter](https://img.shields.io/gitter/room/openspending/chat.svg)](https://gitter.im/openspending/chat)
[![Travis](https://img.shields.io/travis/openspending/os-source-specs.svg)](https://travis-ci.org/openspending/os-source-specs)
[![Pipelines](https://pipelines.openspending.org/badge/collection/source-specs/)](https://pipelines.openspending.org/)

This repository contains `fiscal.source-spec.yaml` files for use by [`os-data-importers`](https://github.com/openspending/os-data-importers), to automate the uploading of fiscal data to [OpenSpending](https://openspending.org/).

## Pipeline status

|Country|Status|
|---|---|
|Burkina Faso|[![Burkina Faso](https://pipelines.openspending.org/badge/collection/source-specs/os-source-specs/africa/burkina-faso)](https://pipelines.openspending.org/source-specs/os-source-specs/africa/burkina-faso)|
|Croatia|[![Croatia](https://pipelines.openspending.org/badge/collection/source-specs/os-source-specs/europe/croatia)](https://pipelines.openspending.org/source-specs/os-source-specs/europe/croatia)|
|Dominican Republic|[![Dominican Republic](https://pipelines.openspending.org/badge/collection/source-specs/os-source-specs/america/dominican-republic)](https://pipelines.openspending.org/source-specs/os-source-specs/america/dominican-republic)|
|Mexico|[![Mexico](https://pipelines.openspending.org/badge/collection/source-specs/os-source-specs/america/mexico)](https://pipelines.openspending.org/source-specs/os-source-specs/america/mexico)|

## How can I contribute fiscal specs?

To update or add new specs, fork this repository, and create a directory for your country within the appropriate top-level directory, then add a valid `fiscal.source-spec.yaml` file. The fiscal spec file defines data sources and processing steps for use by [`os-data-importers`](https://github.com/openspending/os-data-importers) to download, process, and create a fiscal datapackage for OpenSpending.

Please submit changes via a Pull Request to this repository. All `fiscal.source-spec.yaml` files must validate against the `schema.json` json-schema file before they can be merged.

You can test your fiscal spec by creating a Pull Request, or locally with the node application [pajv](https://github.com/json-schema-everywhere/pajv):

```sh
$ npm install -g pajv
$ pajv -s schema.json -d "<continent>/<country>/fiscal.source-spec.yaml"
```
