"""Module to help with adapters and database splits that use mongo db and
more exactly pymongo as driver to connect to"""

from .pymongo_helper import BasicPymongoHelper

__all__ = ["BasicPymongoHelper"]
