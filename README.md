# Introduction

This is a crawler for naftemporiki.gr online newspaper. The output of this crawler
is written in plain text files. The files are stored under directories with the
format `yyyy-mm-dd` and the actual files are named using the following: `<hash>.html`.

# Usage

## Requirements

You need to have these installed to run the project.

- Python 2.x
- pip
- virtualenv

## Prepare \& Run

    $ virtualenv naftis_env
    $ source naftis_env/bin/activate
    $ pip install -r requirements.txt
    $ python src/app.py -d tmp -t 10 -l links.txt 

If you are using Docker you can use the `Dockerfile` you will find in the
repository.

    $ cd naftis
    $ (sudo) docker build -t="naftis" .
    $ (sudo) docker run naftis


# License

The MIT License (MIT)

Copyright (c) 2016 ipinak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
