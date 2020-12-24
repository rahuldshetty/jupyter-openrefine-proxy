import setuptools

setuptools.setup(
    name="jupyter-openrefine-proxy",
    version='0.1',
    url="https://github.com/rahuldshetty/jupyter-openrefine-proxy",
    author="Rahul D Shetty",
    description="Jupyter extension to proxy Open Refine",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'openrefine = jupyter_openrefine_proxy:setup_openrefineserver'
        ]
    }
)
