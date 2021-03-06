import pathlib
import versioneer

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

install_requires = []

setup(
    name="pplots",
    version=versioneer.get_version(),
    description="Plotting for the ptypes package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astrogewgaw/pplots",
    author="Ujjwal Panda",
    author_email="ujjwalpanda97@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    keywords=("pulsars", "plotting"),
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_package_data=True,
    python_requires=">=3.5, <4",
    install_requires=install_requires,
    project_urls={
        "Source": "https://github.com/astrogewgaw/pplots",
        "Bug Reports": "https://github.com/astrogewgaw/pplots/issues",
    },
    cmd_class=versioneer.get_cmdclass(),
    zip_safe=False,
)
