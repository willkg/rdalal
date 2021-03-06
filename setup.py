from setuptools import find_packages, setup
import sys


setup(
    name="rdalal",
    version="1.2.0",
    description="Install some sweet Rehan",
    author="Will Kahn-Greene",
    author_email="willkg@bluesock.org",
    url="https://github.com/willkg/rdalal",
    zip_safe=True,
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        rdalal=rdalal.cmdline:run
    """,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)


if "install" in sys.argv or "bdist_wheel" in sys.argv:
    import webbrowser

    # NOTE(willkg): "pip install" will capture stdout here, so this doesn't get
    # printed to the user.
    print("")
    print("You've installed rdalal! Time for some sweet tunes!")
    webbrowser.open(
        "https://www.youtube.com/watch?v=NMZcwXh7HDA", new=2, autoraise=True
    )
