from setuptools import setup

setup(
   name='deepgp_dsvi',
   version='1.0',
   description='Doubly-Stochastic VI for Deep GPs',
   author='Hugh Salimbeni, Felix Opolka',
   author_email='felix.opolka@gmail.com',
   packages=['deepgp_dsvi'],  #same as name
   install_requires=['gpflow>=2.0'], #external packages as dependencies
)
