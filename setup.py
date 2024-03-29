from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='funniest joke comedy flying circus',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['funniest'],
      scripts=['bin/funniest-joke'],
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False)