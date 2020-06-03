from tiepy import overrides, final


class BaseClass:
    def my_method(self):
        pass


class ExtensionClass(BaseClass):
    @overrides
    def my_method(self):
        pass
