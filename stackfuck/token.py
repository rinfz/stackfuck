class Token(object):

    def __init__(self, **kwargs):
        assert 'type' in kwargs
        assert 'value' in kwargs

        self.__dict__.update(kwargs)
