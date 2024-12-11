"""A Collection of Excaptions for the RedHat insight API"""


class RHAPIConnectionError(Exception):
    """Connection Error for RedHat API"""


class RHAPINoTokenError(Exception):
    """API Token not set"""
