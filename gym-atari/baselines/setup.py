from setuptools import setup, find_packages
import sys

if sys.version_info.major != 3:
    print('This Python is only compatible with Python 3, but you are running '
          'Python {}. The installation will likely fail.'.format(sys.version_info.major))


setup(name='baselines',
      packages=[package for package in find_packages()
                if package.startswith('baselines')],
      install_requires=[
          'gym[atari,classic_control]==0.13.1',
          'scipy',
          'tqdm',
          'joblib',
          'dill',
          'progressbar2',
          'mpi4py',
          'cloudpickle',
          'tensorflow==1.13.1',
          'click',
          'opencv-python',
      ],
      extras_require={
        'test': [
            'filelock',
            'pytest'
        ]
      },
      description='OpenAI baselines: high quality implementations of reinforcement learning algorithms',
      author='OpenAI',
      url='https://github.com/openai/baselines',
      author_email='gym@openai.com',
      version='0.1.5')
