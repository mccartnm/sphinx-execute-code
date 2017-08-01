from distutils.core import setup

setup(
        name='sphinx_execute_code',
        version='0.2a1',
        platforms=['any'],
        packages=['sphinx_execute_code'],
        url='https://github.com/jpsenior/sphinx-execute-code',
        license='MIT',
        author='JP Senior',
        author_email='jp.senior@gmail.com',
        description='Sphinx support for execution of python code in sphinx documentation from code blocks or files',
        requires=['docutils'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Framework :: Sphinx :: Extension',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 2.7',
        ],
        keywords='sphinx extension directive execute code',
)