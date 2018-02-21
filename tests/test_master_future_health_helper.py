from freezegun import freeze_time
class Foo:
    @freeze_time('2018-01-01')
    def qux(self):
        pass

    def quux(self):
        pass
