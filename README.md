<img src="https://github.com/ds1219/harisum/blob/main/assets/logo.svg" alt="drawing" width="200"/> 
## harisum

A cross-platform python tool (gui + cmd) to generate and verify file checksums.

## BUILD EXE
### install dependancies
```
pip install tqdm pysimplegui pyinstaller
```

### build gui
```
pyinstaller py-hs.spec
```
Executable will be generated into the ```dists``` filder

## CMD Usage

```
hs.py <file> <algo> <key>
```

### Dependancies :

#### tqdm

```
pip install tqdm
```

**for best experience use a shell that supports coloured output! (ANSI escape codes)**

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
