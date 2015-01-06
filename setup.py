from setuptools import find_packages, setup
import sys


# Installing rdalal will open the video in your browser.
if 'egg_info' in sys.argv or 'install' in sys.argv:
    import webbrowser
    webbrowser.open('https://www.youtube.com/watch?v=NMZcwXh7HDA', new=2, autoraise=True)


setup(
    name='rdalal',
    version='1.0',
    description='Install some sweet Rehan',
    author='Will Kahn-Greene',
    author_email='willkg@bluesock.org',
    url='https://github.com/willkg/rdalal',
    zip_safe=True,
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        rdalal=rdalal.cmdline:run
    """,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
