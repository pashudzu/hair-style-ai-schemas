from setuptools import setup, find_packages

setup(
    name="hair-style-ai-schemas",
    version="0.0.5",
    author="pashudzu",
    author_email="pashudzu@gmail.com",
    description="Library of schemas for project hair-style-ai",
    project_urls={"GitHub": "https://github.com/pashudzu/hair-style-ai-schemas"},
    packages=find_packages(),
    install_requires=["pydantic"],
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["auth", "generate"],
    python_requires=">=3.6",
)