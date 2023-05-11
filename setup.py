from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_library/__init__.py
from frappe_library import __version__ as version

setup(
	name="frappe_library",
	version=version,
	description="desc",
	author="me",
	author_email="my@email.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
