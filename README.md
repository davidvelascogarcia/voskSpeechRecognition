[![voskSpeechRecognition Homepage](https://img.shields.io/badge/voskSpeechRecognition-develop-orange.svg)](https://github.com/davidvelascogarcia/voskSpeechRecognition/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/voskSpeechRecognition.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/voskSpeechRecognition/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/voskSpeechRecognition.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/voskSpeechRecognition)

# Vosk Speech Recognition: voskSpeechRecognition (Python API)

- [Introduction](#introduction)
- [Use](#use)
- [Requirements](#requirements)
- [Status](#status)
- [Related projects](#related-projects)


## Introduction

`voskSpeechRecognition` module use `Vosk Speech Recognition API` in `python`. This module performs speech recognition using `Kaldi` speech recognition backend and converts to text. Also use `YARP` to send text detection by network. Also admits `YARP` source audio like input. This module also publish recognition results in `YARP` port. `voskSpeechRecognition` require models to perform the module. Some pre-trained models in english, spanish, chinese, russian, french, german, portuguese, greek, turkish, vietnamese are available in [vosk models](https://alphacephei.com/vosk/models.html). 

## Use

`voskSpeechRecognition` requires audio like input.`voskSpeechRecognition` models should be located in `voskSpeechRecognition/models/model-x`, being `x` your selected language. Download [vosk models](https://alphacephei.com/vosk/models.html) and extract content in your `model-x` dir. Also configure [language.ini](./config/language.ini) with your `x` selected language.

The process to running the program:

1. Execute [programs/voskSpeechRecognition.py](./programs), to start de program.
```python
python3 speechRecognition.py
```
2. Connect recognition source.
```bash
yarp connect /voskSpeechRecognition/data:o /yourport/data:i
```

**Language table:**

Table 1. Language table

| Language | x |
|---|---|
| Spanish | es |
| English | en |
| Chinese | cn |
| Russian | ru |
| French | fr |
| German | de |
| Portuguese | pt |
| Greek | gr |
| Turkish | tr |
| Vietnmaese | vn |


**NOTE:**

- Data results are published on `/voskSpeechRecognition/data:o`

**Possible errors:**

`vosk` `python` version requirements:

- `vosk` require `python 3.8+` to be used in `Windows`.
- `vosk` require `python 3.5+` to be used in `Linux`.
- `vosk` require `python 3.8+` to be used in `Mac OS X`.
- `vosk` require `python 3.7+` to be used in `Raspbian`. (`Raspberry` also require to download and install `.whl` manually. `vosk` `Raspberry` version [here](https://github.com/alphacep/vosk-api/releases/download/0.3.7/vosk-0.3.7-cp37-cp37m-linux_aarch64.whl)


## Requirements

`voskSpeechRecognition` requires:

* [Install YARP 2.3.XX+](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-yarp.md)
* [Install pip](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)
* Install vosk:

```bash
pip3 install vosk
```

Tested on: `windows 10`, `ubuntu 14.04`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `raspbian`.


## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/voskSpeechRecognition.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/voskSpeechRecognition)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/voskSpeechRecognition.svg?label=Issues)](https://github.com/davidvelascogarcia/voskSpeechRecognition/issues)

## Related projects

* [Alpha Cephei: vosk speech recognition](https://alphacephei.com/vosk/)

