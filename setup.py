try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='xgboost',
    version='0.81',
    description='XGBoost is an optimized distributed gradient boosting library.',
    url='https://github.com/Shopify/xgboost',
    packages=['sparkxgb'],
    include_package_data=True,
    install_requires=[
    ],
    license="Apache 2.0",
    zip_safe=True,
    keywords='xgboost'
)
