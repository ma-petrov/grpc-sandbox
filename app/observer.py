class Observer():
    def __init__(self, name):
        self.name = name

    def update(self):
        raise NotImplementedError('Method update not implemented')

class Observable():
    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        if not isinstance(observer, Observer):
            raise TypeError()
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)