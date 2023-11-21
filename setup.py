from setuptools import setup, find_packages

setup(
    name='writing_style_converter',
    version='1.0.1',
    packages=find_packages(),
    author='Stepan Orlov',
    description='A library for converting naming styles in Python code.',
    long_description='''The writing_style_converter library provides convenient tools for converting between various naming styles (e.g., snake_case, kebab_case, camel_case, pascal_case) in Python code. Streamline the process of handling different naming conventions in models, APIs, and more. Check out the [GitHub repository](https://github.com/OrlovSA/writing_style_converter/blob/main/README.md) for usage examples and detailed documentation. Telegram @Orlov_SA''',
    long_description_content_type='text/markdown',
    author_email='stepan.nadym@gmail.com',
    license="MIT License"
)
