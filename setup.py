''' Config file for setuptools '''
from setuptools import setup

setup(
    name='get_some_rest',
    version='0.1',
    py_modules=['ica_var', 'bst2mne', 'meg2mat',
                'get_conmat', 'add_age', 'get_powers',
                'collect_neuropype'],
    install_requires=[
        'Click', 'mne'
    ],
    entry_points='''
        [console_scripts]
        ica_var=ica_var:cli
        bst2mne=bst2mne:cli
        psd2bandpower=psd2bandpower:cli
        meg2mat=meg2mat:cli
        get_conmat=get_conmat:cli
        add_age=add_age:cli
        get_powers=get_powers:cli
        collect_neuropype=collect_neuropype:cli
    ''',
)
