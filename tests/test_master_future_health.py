from freezegun import freeze_time
class Foo:
    @freeze_time('2018-01-01')
    def bar(self):
        pass
        
    def baz(self):
        pass
