Amateur Packet Radio
====================

This is a client for the Amateur Packet Radio (AMPR) Portal API. You need
to be a license HAM radio amateur and you need to have a `AMPR Portal`_ 
account in order to use this package.

Once you have an account, nagivate to the `AMPR Portal Profile`_ page, and
look for your API Key, if there is none, you can generate a 32 character
secret and save it in your profile. You can generate such key with Python
easily::

    >>> import string
    >>> import random
    >>> print(''.join(random.choice(chars) for x in range(32)))
    ahdX3fOskC9gGYcyxOfYNyLZEVqD54fC

Don't use the secret above, generate your own.

.. _AMPR Portal: https://portal.ampr.org/
.. _AMPR Portal Profile: https://portal.ampr.org/profile.php
