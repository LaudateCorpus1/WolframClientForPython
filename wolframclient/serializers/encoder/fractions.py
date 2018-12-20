# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals
from wolframclient.serializers.encoder import wolfram_encoder
import fractions

@wolfram_encoder.dispatch(fractions.Fraction)
def encode_faction(serializer, o):
        return serializer.serialize_fraction(o)
