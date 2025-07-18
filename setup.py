from setuptools import setup, find_packages

setup(
    name="code_converter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'openai>=1.0.0',
        'anthropic>=0.7.0',
        'gradio>=4.0.0',
        'python-dotenv>=1.0.0',
    ],
    python_requires='>=3.8',
)
