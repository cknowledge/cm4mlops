﻿[ [Back to documentation](README.md) ]

*Under development*

# CM Getting Started Guide

## Image classification example

One of the goals of the [MLCommons CM workflow automation framework (CM)](https://github.com/mlcommons/ck?tab=readme-ov-file#about) 
is to provide a common, simple and human readable interface to run and manage complex software projects and benchmarks 
on any platform with any software stack in a unified and automated way.

This tutorial explains how CM works and should help you start using it with existing projects 
or to modularize and unify your own projects.

Let us test CM to run image classification from the command line on any platform with Windows, Linux and MacOS.

### Installing CM

CM is implemented as a [very small Python library](https://github.com/mlcommons/ck/tree/master/cm/cmind) 
with `cm` and `cmr` front-ends and minimal dependencies (Python 3+, git and wget) 
that can be installed via PIP:


```bash
pip install cmind
```

You may need to re-login to update the PATH to `cm` and `cmr` front-ends.

Note that CM can be also installed from virtual environment (required in Ubuntu 23.04+) and inside containers.
You can check a detailed guide to install CM on different platforms [here](installation.md).

### Pulling some repository with embedded CM interface

Let's now pull a Git repository that has embedded CM interface 
(note that if your Git repository doesn't have CM interface embedded,
CM will automatically initialize one):

```bash
cm pull repo mlcommons@ck
```

CM will pull GitHub repository from `https://github.com/mlcommons/ck` to the `CM/repos` directory in your local HOME directory.
You can use flag `--url=https://github.com/mlcommons/ck` instead of `mlcommons@ck` to pull any Git repository.

CM will then check if this repository has a CM interface by checking the [`cmr.yaml`](https://github.com/mlcommons/ck/blob/master/cmr.yaml) 
file in the root directory of this repository (abbreviation for `C`ollective `M`ind `R`epository):

```yaml
git: true
alias: mlcommons@ck
uid: a4705959af8e447a
version: 1.5.4
prefix: cm-mlops
```

Note that this file will be automatically generated if it doesn't exist in your repository.

While working on modularizing, unifying and automating MLPerf benchmarks,
we decided to embed a CM interface to this development repository 
in the [cm-mlops directory](https://github.com/mlcommons/ck/tree/master/cm-mlops)

The `prefix` in `cmr.yaml` tells CM to search for the CM interface in some sub-directory of a given repository
to avoid altering the original structure of software projects.

### Using CM interface to run a given software project

You can now invoke a human-friendly CM command to run your project such as image classification
(we will show how to use Python API later):

```bash
cm run script "python app image-classification onnx"
```

CM will recursively walk through all pulled or downloaded repositories in your home `CM/repos` directory
and search for matching tags `python,app,image-classification,onnx` in all `_cm.yaml` or `_cm.json`
files in a `script` sub-directory of all repositories.

In our case, CM will find 1 match in 
the [`cm-mlops/script/app-image-classification-onnx-py/_cm.yaml`](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml).

This file tells CM how to prepare environment variables, paths and command lines 
to run a native script or tool on any platform.


#### 












#### Using inputs and environment variables

env

const


default_env

input_mapping



#### Using variations

using the same code/script/tool but altering it's behavior and sub-dependencies

CUDA

_cuda


#### Reporting issues

The community helped us test this example on many platforms but if you still encounter
some issues, please report them [here](https://github.com/mlcommons/ck/issues) - CM is not a magic (yet)
and our concept is to collaboratively extend CM workflows to gradually improve their portability and reproducibility
across diverse software and hardware.



#### Debugging CM interface


#### Extending CM interface


### Reusing automation recipes



### Adding CM interface to your own project



### Using CM with containers


### Using CM GUI


### Running MLPerf and other projects via CM 

Recent examples from MLPerf and ML, compiler and systems conferences


### Participating in collaborative developments

This is a community project being developed by the [MLCommons Task Force on Automation and Reproducibility](taskforce.md)
based on your feedback - please join our [public Discord server](https://discord.gg/JjWNWXKxwT) if you 
would like to help with developments or have questions, suggestions and feature requests.