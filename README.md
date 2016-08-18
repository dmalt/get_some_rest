# Installation

```bash
$ git clone https://github.com/dmalt/get_some_rest.git
$ cd get_some_rest
$ pip install --editable .
```

# Utilities

## ica_var 
Show explained variance for mne-python ICA solution

##### Examples:
```bash
$ ica_var ./MEG2016/*/*-ica.fif >> vars.txt
```

## bst2mne
Convert epochs from brainstorm protocol in .mat format to mne.Epochs object and save to a file

##### Options:

	  -s, --savename TEXT

	  --rec-type [ds|fif]

	  -i, --infosrc TEXT   file to take info from

	  --help               Show this message and exit.

##### Examples:
```bash
$ bst2mne ~/Documents/dmalt_sample_epochs/data*.mat -s ${PWD##*/}-epo.fif -i Control01_Open.ds
```