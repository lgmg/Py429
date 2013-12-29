__author__ = 'nicolas'

import Bus
import datetime
import Message
import DiscreteBit
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
from _version import __version__


def serialize(stream, objectToSerialize):

    #TODO: add try

    generated_on = str(datetime.datetime.now())
    top = objectToSerialize.serialize(stream)
    top.append(Comment('Generated by {} [{}] on -{}-'.format(__name__.rpartition('.')[0], __version__, generated_on)))

    ElementTree(top).write(stream)


if __name__ == "__main__":

    testBus = Bus.Bus('testBus')

    testMessage1 = Message.Message('baseMessage', 'odd')
    testMessage1.setLabel('257')
    testMessage1.addField(DiscreteBit.Field(10,'testBit','test bit is happy','test bit is not happy'))
    testMessage1.addField(DiscreteBit.Field(15,'bobo','test bit is happy','test bit is not happy'))

    with open("/home/nicolas/Desktop/test.xml",'w') as XMLFile:
        serialize(XMLFile,testBus)
