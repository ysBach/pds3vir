# pds3vir
An extremely simple PDS3 format "VICAR .img file reader" (vir).

Currently this repo contains effectively only one python file, vicar.py, which is heavily inherited from [``SETI/pds-tools/vicar.py``](https://github.com/SETI/pds-tools) (permalink for the specific commit: [@21dc09c](https://github.com/SETI/pds-tools/blob/3690697fa166a686d6526f195567f180c7593543/vicar.py#L1)). The initial

Few differences:
- **Requires python 3.8 or later**
- Made it as a package.
- Minor tuning to the internal codes (see "history" of the file).
- Remove deprecated attributes.
