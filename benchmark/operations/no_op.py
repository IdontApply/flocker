from pyrsistent import PClass, field
from zope.interface import implementer

from twisted.internet.defer import succeed

from .._operations import IProbe, IOperation


@implementer(IProbe)
class NoOpProbe(PClass):
    """
    A probe that performs no operation.
    """

    def run(self):
        return succeed(None)

    def cleanup(self):
        return succeed(None)


@implementer(IOperation)
class NoOperation(PClass):
    """
    An nop operation.
    """

    control_service = field(mandatory=True)

    def get_probe(self):
        return NoOpProbe()
