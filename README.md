![alt text](https://github.com/ds1219/harisum/blob/main/assets/logo.svg)

# harisum

A cross-platform python tool (gui + cmd) to generate and verify file checksums.

## CMD Usage

```
hs.py <file> <algo> <key>
```

### Dependancies :

#### tqdm

```
pip install tqdm
```

**for best experience use a shell that supports ANSI escape codes**

## GUI Usage

Open hs-gui

```
python hs-gui.py
```

### Dependancies:

#### pysimplegui

```
pip install pysimplegui
```

#### tkinter

tkinter is usually included with the standard python installation, but some linux distros do not include it by default.

## Supported checksum algorithms:

- SHA1
- SHA256
- MD5
