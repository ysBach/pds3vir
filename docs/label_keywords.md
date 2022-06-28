VICAR LABEL STRUCTURE

The VICAR label is a string of ASCII characters consisting of free-field items of the form ``keyword=value`` separated by spaces. It contains data set description system information regarding the dimensions, organization and data format. This information is written to the label with the following keywords:

* ``LBLSIZE``: Size of the label in bytes
* ``FORMAT``: Data format (byte, halfword, real, fullword, etc.)
* ``TYPE``: Data set type (image, parameter, histogram, plot, etc.)
* ``BUFSIZ``: Internal blocksize VICAR will use during input/output
* ``DIM``: Data set dimension
* ``EOL``: End-of-dataset label
* ``RECSIZE``: Data set record size
* ``ORG``: Data set organization:
* ``BSQ``: - Band Sequential
* ``BIL``: - Band Interleaved by Line
* ``BIP``: - Band Interleaved by Pixel
* ``NL``: Number of lines or records
* ``NS``: Number of samples or record length
* ``NB``: Number of bands or number of data planes
* ``NBB``: Number of binary prefix bytes
* ``NLB``: Number of binary header records
* ``N1``: Equal to NS
* ``N2``: Equal to NL for BSQ, NB for BIL and NS for BIP
* ``N3``: Equal to NB for BSQ, or NL for BIL and BIP
* ``N4``: Not used
* ``HOST``: Type of computer used to generate the image.
* ``INTFMT``: The format used to represent integers in the file.
* ``REALFMT``: The format used to represent floating numbers.
* ``BHOST``: Type of computer used to generate the binary information.
* ``BINTFMT``: The format used to represent binary integers in the file.
* ``BREALFMT``: The format used to represent binary floating numbers.
* ``BLTYPE``: The binary label type. Currently not implemented.
