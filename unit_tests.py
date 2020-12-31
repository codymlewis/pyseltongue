# -*- coding: utf-8 -*-
"""
    Secret Sharing
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

import random
import unittest
from test import support
from utilitybelt import base64_chars
from pyseltongue import SecretSharer, PlaintextToHexSecretSharer, \
    BitcoinToB58SecretSharer, BitcoinToB32SecretSharer, \
    BitcoinToZB32SecretSharer

class ShamirSharingTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def split_and_recover_secret(self, sharer_class, m, n, secret):
        shares = sharer_class.split_secret(secret, m, n)
        random.shuffle(shares)
        recovered_secret = sharer_class.recover_secret(shares[0:m])
        assert(recovered_secret == secret)

    def split_and_recover_secret_alt_parts(self, sharer_class, m, n, secret):
        shares = sharer_class.split_secret(secret, m, n)
        length_of_shares = len(shares)
        if length_of_shares > 2:
            # print("\n", shares[length_of_shares-m:])
            recovered_secret = sharer_class.recover_secret(
                shares[length_of_shares-m:]
            )
        else:
            recovered_secret = sharer_class.recover_secret(shares[0:m])
        assert(recovered_secret == secret)

    def test_hex_to_hex_sharing(self):
        self.split_and_recover_secret(
            SecretSharer, 3, 5,
            "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )
        self.split_and_recover_secret_alt_parts(
            SecretSharer, 3, 5,
            "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )

    def test_printable_ascii_to_hex_sharing(self):
        self.split_and_recover_secret(
            PlaintextToHexSecretSharer, 3, 5,
            "correct horse battery staple"
        )
        self.split_and_recover_secret_alt_parts(
            PlaintextToHexSecretSharer, 3, 5,
            "correct horse battery staple"
        )

    def test_zero_leading_ascii_to_hex_sharing(self):
        self.split_and_recover_secret(
            PlaintextToHexSecretSharer, 3, 5,
            '0B4A30EEFEBA6783EA68F79AD5DC85E4DDCD83D4'
        )
        self.split_and_recover_secret_alt_parts(
            PlaintextToHexSecretSharer, 3, 5,
            '0B4A30EEFEBA6783EA68F79AD5DC85E4DDCD83D4'
        )

    def test_b58_to_b32_sharing(self):
        self.split_and_recover_secret(
            BitcoinToB32SecretSharer, 3, 5,
            "5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS"
        )
        self.split_and_recover_secret_alt_parts(
            BitcoinToB32SecretSharer, 3, 5,
            "5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS"
        )

    def test_b58_to_zb32_sharing(self):
        self.split_and_recover_secret(
            BitcoinToZB32SecretSharer, 3, 5,
            "5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS"
        )
        self.split_and_recover_secret_alt_parts(
            BitcoinToZB32SecretSharer, 3, 5,
            "5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS"
        )

    def test_b58_to_b58_sharing(self):
        self.split_and_recover_secret(
            BitcoinToB58SecretSharer, 3, 5,
            "5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS"
        )
        self.split_and_recover_secret_alt_parts(
            BitcoinToB58SecretSharer, 3, 5,
            "5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS"
        )

    def test_hex_to_base64_sharing(self):
        sharer_class = SecretSharer
        sharer_class.share_charset = base64_chars
        self.split_and_recover_secret(
            sharer_class, 3, 5,
            "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )
        self.split_and_recover_secret_alt_parts(
            sharer_class, 3, 5,
            "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )

    def test_2_of_3_sharing(self):
        self.split_and_recover_secret(
            SecretSharer, 2, 3,
            "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )
        self.split_and_recover_secret_alt_parts(
            SecretSharer, 2, 3,
            "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )

    def test_4_of_7_sharing(self):
        self.split_and_recover_secret(
            SecretSharer, 4, 7,
            "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )
        self.split_and_recover_secret_alt_parts(
            SecretSharer, 4, 7,
            "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )

    def test_5_of_9_sharing(self):
        self.split_and_recover_secret(
            SecretSharer, 5, 9,
            "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )
        self.split_and_recover_secret_alt_parts(
            SecretSharer, 5, 9,
            "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )

    def test_2_of_2_sharing(self):
        self.split_and_recover_secret(
            SecretSharer, 2, 2,
            "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )
        self.split_and_recover_secret_alt_parts(
            SecretSharer, 2, 2,
            "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )


def test_main():
    support.run_unittest(
        ShamirSharingTest
    )


if __name__ == '__main__':
    test_main()
