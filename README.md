# Dots SDK for Python

The Dots Python library provides convenient access to the Dots API from applications written in the Python language.

## Documentation

See the [API docs](https://docs.senddots.com).

## Installation

To install the package run:
```
pip install --upgrade dots-python
```

Install from source with:
```
python setup.py install
```

## Usage

The library needs to be configured with your `client_id` and `api_key` which can be found in the [Developer Dashboard](https://www.senddots.com/developer)

```
import dots
dots.client_id = 'pk_dev_...'
dots.api_key = 'sk_dev_...'

invoice = dots.Invoice.create(...)
```
