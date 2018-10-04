# Juju charm template
This repository is a simple tool to add additional template(s) to charmtools.
The intention is for testing and development of templates before requesting
inclusion of the teamplate in the standard tools.

## Installation / Usage
This is not currently available via a snap, because it was started for development not
intended to be a long term solution. It requires charmtools as it's implemented
as a monkeypatch on charmtools. 

To install charmtools:
```bash
sudo snap install charm
```

Clone this repository:
```bash
git clone https://github.com/chris-sanders/charm-template.git
```

You can now run the incldued charm-template tool to create templates with the
new template python-pytest.
```bash
cd charm-template
./charm-create.py -t python-pytest my-example
```
