import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="workdown",
    version="0.0.4",
    author="Eldridge Alexander",
    author_email="eldridgea@gmail.com",
    description="Write Markdown and have it published and hosted on Cloudflare Workers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eldridgea/workdown",
    packages=setuptools.find_packages(),
    install_requires=['markdown'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
        entry_points={
        'console_scripts': [
            'workdown = workdown.workdown:main'
        ]
    },
)