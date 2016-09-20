# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T


class SortOrder(T.Enum):
    """
    One of ['ascending', 'descending', 'none']
    """
    def __init__(self, default_value=T.Undefined, **metadata):
        super(SortOrder, self).__init__(['ascending', 'descending', 'none'],
                                    default_value=default_value,
                                    **metadata)