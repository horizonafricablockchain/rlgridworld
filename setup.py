import setuptools

# even though the unreasonable "security reason" https://github.com/pypa/pip/issues/6301 bans direct install from setup.py, we should manage to install it with pip install -r

def get_extra_requires(path, add_all=True):

    with open(path) as fp:
        extra_deps = {}
        for s in fp:
            s = s.split('#')[0] # remove comments
            if s.strip():
                if ';' in s:
                    v, k = s.split(';')
                    v = v.strip()
                    for sub_key in k.split(','):
                        sub_key = sub_key.strip()
                        if sub_key in extra_deps:
                            extra_deps[sub_key].append(v)
                        else:
                            extra_deps[sub_key] = [v]
                        if 'all' in extra_deps:
                            extra_deps['all'].append(v)
                        else:
                            extra_deps['all'] = [v]

    return extra_deps

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read()

# Add d3rlpy to the requirements list
requirements += '\nd3rlpy'

setuptools.setup(
    name='rlgridworld',
    version='0.1004',
    author="Mohan Zhang",
    author_email="mohan.zhang.mz@gmail.com",
    description="This is a simple yet efficient, highly customizable grid-world implementation to run reinforcement learning algorithms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mohan-Zhang-u/rlgridworld",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    # extras_require=get_extra_requires('extras_requirements.txt'),
)