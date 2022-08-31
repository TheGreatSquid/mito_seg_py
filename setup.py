import setuptools

setuptools.setup(
    name='mito_seg_py',
    version='0.0.1',
    author='Paul Morenkov',
    packages=['mito_seg_py'],
    install_requires=[
        'keras>=2.3.0',
        'tensorflow>=1.14.0',
    ]
)