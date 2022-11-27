# Ops-Utils

Collection of simple utilities for cloud/system operators. They follow the philosophy of Unix: pipes

# Utilities

## delta-iso-timestamps.py

```
usage: delta-iso-timestamps.py [-h] [--summary] [--no-summary] [FILE ...]

Accepts a list of ISO timestamps via STDIN and prints the delta between each timestamp. 
 
Example: 
 
echo "2022-11-26 16:54:30.313\n2022-11-26 16:54:30.321" | ./delta-iso-timestamps.py

positional arguments:
  FILE          files to read, if empty, stdin is used

options:
  -h, --help    show this help message and exit
  --summary
  --no-summary
```

