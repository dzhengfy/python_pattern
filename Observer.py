#! /usr/bin/python

class E_commerce(object):
    """
    Base subject class, implement register/unregister, notify
    """

    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def delete_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
        else:
            raise Exception('%s observer not be monitored' % observer)

    def notify_all_observers(self, promotion):
        for observer in self._observers:
            observer.update(self, promotion)


class A_shop(E_commerce):
    """
    Real subject class being observed
    """

    def __init__(self):
        super(A_shop, self).__init__()
        self._promotion = []  # Promotion list

    def __str__(self):
        return 'A_shop'

    @property
    def promotion(self):
        "return promotion list"
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        self._promotion.append(promotion)  # add new promotion
        self.notify_all_observers(promotion)  # notify observers about the promotions


class Observer(object):
    """
    Abstract class for observer, define update function
    """

    def update(self, *args, **kwargs):
        pass


class A_customer(Observer):
    """
    A implements update function
    """

    def update(self, e_commerce, promotion):
        print('to a_customer: {} is doing {}'.format(e_commerce, promotion))


class B_customer(Observer):
    """
    B implements update function
    """

    def update(self, e_commerce, promotion):
        print('to b_customer: {} is doing {}'.format(e_commerce, promotion))


if __name__ == '__main__':
    """
    Please use observer pattern to complete the client codes
    Below outputs are expected:
    to a_customer: A_shop is doing first discount
    to b_customer: A_shop is doing first discount
    to a_customer: A_shop is doing second discount
    to b_customer: A_shop is doing second discount
    to b_customer: A_shop is doing third discount

    """
