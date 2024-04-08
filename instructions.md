## Development Instructions

For every python project you need to have an environment. To create one you need:

```sh

python -m venv venv   


```

To use the environment you need:

```sh
source venv/bin/activate   

```

To install the dependencies you need:
```sh
pip install -r requirements.txt
```

If you need to generate the dependencies again you need:

```sh
pip freeze > requirements.txt
```