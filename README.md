About s3copy
========
Install
---------
```bash
python -m pip install git+https://github.com/fluidstackio/s3copy
```

Run
---
First place the aws ACCESS_KEY and SECRET_KEY in environmental variables
then run:

```bash
python3 -m s3copy.app imagename bucket-name
```