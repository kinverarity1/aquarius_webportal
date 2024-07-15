from setuptools import setup

TEST_REQS = (
    "pytest>=3.6",
    "pytest-cov",
    "coverage",
    "codecov",
    "pytest-benchmark",
    "black",
    "sphinx",
    "nbsphinx",
)

setup(
    name="aquarius_webportal",
    packages=("aquarius_webportal",),
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="Python code to get data from implementations of Aquarius Web Portal",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kinverarity1/aquarius_webportal",
    author="Kent Inverarity",
    author_email="kinverarity@hotmail.com",
    license="MIT",
    install_requires=("requests", "pandas>=0.24.1", "lxml"),
    extras_require={
        "test": (TEST_REQS,),
    },
    tests_require=(TEST_REQS),
    python_requires=">=3.7",
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ),
    keywords="python groundwater data-access surface-water",
)
