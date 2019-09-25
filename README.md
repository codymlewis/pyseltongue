Pyseltongue
=============

[![PyPI](https://img.shields.io/pypi/v/pyseltongue.svg)](https://pypi.python.org/pypi/pyseltongue/)
[![PyPI](https://img.shields.io/pypi/dm/pyseltongue.svg)](https://pypi.python.org/pypi/pyseltongue/)
[![PyPI](https://img.shields.io/pypi/l/pyseltongue.svg)](https://github.com/ginsburgnm/pyseltongue/blob/master/LICENSE)

A library for sharding and sharing secrets (like Bitcoin private keys), using shamir's secret sharing scheme.

## Name
I shamelessly stole this name idea from a coworker, shamir-secret-sharing-service ssss -> parseltongue -> we're in python -> pyseltongue (nagini was already taken)

## History Disclaimer
This was initially forked from [secret-sharing](https://github.com/blockstack/secret-sharing) but they haven't updated the package in 4 years much to many people's dismay. It was getting a little irritating that github kept defaulting to opening merge requests to their repo, even though that will never happen. 

The code has been updated to python3 capatibility and I hope it is useful for others.

## Installation

    >>> pip install pyseltongue

## Sample Usage

### Hex Secrets

#### Splitting into shares
    
    >>> from pyseltongue import SecretSharer
    >>> shares = SecretSharer.split_secret("c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a", 2, 3)
    ['1-58cbd30524507e7a198bdfeb69c8d87fd7d2c10e8d5408851404f7d258cbcea7', '2-ecdbdaea89d75f8e73bde77a46db821cd40f430d39a11c864e5a4868dcb403ed', '3-80ebe2cfef5e40a2cdefef0923ee2bb9d04bc50be5ee308788af98ff609c380a']

#### Recovering from shares

    >>> SecretSharer.recover_secret(shares[0:2])
    'c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a'

### Plaintext Secrets

#### Splitting into shares

    >>> from pyseltongue import PlaintextToHexSecretSharer
    >>> shares = PlaintextToHexSecretSharer.split_secret("correct horse battery staple", 2, 3)
    ['1-7da6b11af146449675780434f6589230a3435d9ab59910354205996f508b8d0d', '2-fb4d6235e28c892cea70367c15ec3cbfed4cf4a417bd01e9812980f3ac97ddc8', '3-78f41350d3d2cdc35f6868c3357fe74f37568bad79e0f39dc04d687808a42d5a']

#### Recovering from shares

    >>> PlaintextToHexSecretSharer.recover_secret(shares[0:2])
    'correct horse battery staple'

### Bitcoin Private Keys

Note: Bitcoin private keys are in [Base58 check](https://en.bitcoin.it/wiki/Base58Check_encoding) format.

#### Splitting into reliably printable base58 shares

    >>> from pyseltongue import BitcoinToB58SecretSharer
    >>> shares = BitcoinToB58SecretSharer.split_secret("5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS", 2, 3)
    ['2-Bqni1ysZcXhFBhVVJLQgPimDUJrjBrzuvBmc6gPNPh1jyDcvM6uYUuH', '3-9xpMBerBCdHLKzCQ82fjVLfZ3Qt48sqa6nz1E3cc6eu3qUe58vaogU3', '4-85qzMKpnnisRUGuJwivnaxZtcWuP5tgEHQCQMQqqocnMhjfDvkG4t2o']

#### Recovering from base58 shares

    >>> BitcoinToB58SecretSharer.recover_secret(shares[0:2])
    '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS'

#### Splitting into reliably transcribable [base32](http://en.wikipedia.org/wiki/Base32) shares

    >>> from pyseltongue import BitcoinToB32SecretSharer
    >>> shares = BitcoinToB32SecretSharer.split_secret("5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS", 2, 3)
    ['B-RJ6Y56OSUWDY5VAAGC6XLSTM64CAJ2LPBNB7NKATJCWC7VSHIP5DQIVMR6OGJ4GB', 'C-CT5R24XAR5B732JWYQKSYOYBSF5VHI73HLY24QCFRJR5XUW64C4JWYN6SRGWVCUG', 'D-T54KX27OPEAGZ7TNK5WOFK4WFPZKEXUHNKPWLWDXZQNYPT3WPV3P5IGQTD7HAJDG']

#### Recovering from base32 shares

    >>> BitcoinToB32SecretSharer.recover_secret(shares[0:2])
    '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS'  

#### Splitting into reliably transcribable [zbase32](http://philzimmermann.com/docs/human-oriented-base-32-encoding.txt) shares

    >>> from pyseltongue import BitcoinToZB32SecretSharer
    >>> shares = BitcoinToZB32SecretSharer.split_secret("5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS", 2, 3)
    ['b-aweuzkm9jmfgd7x4k595bzcm3er3epf4dprfwzpprqa3exbuocs9byn4owfuqbo', 'n-btetgqqu8doacarsbyfdzpyycyj6gfdeaaxrpfx33pdjk4ou1d5owjdmdi1iegm9', 'd-njh33f14q7smucmh8iq8uaewc8mzub3mzptrwsegfiz3hc1fozkkjtguc4trh6sq']

#### Recovering from zbase32 shares

    >>> BitcoinToZB32SecretSharer.recover_secret(shares[0:2])
    '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS'    

### Raw integers

#### Splitting into shares

    >>> from pyseltongue import secret_int_to_points, points_to_secret_int
    >>> secret = 88985120633792790105905686761572077713049967498756747774697023364147812997770L
    >>> shares = secret_int_to_points(secret, 2, 3)
    [(1, 108834987130598118322155382953070549297972563210322923466700361825476188819879L), (2, 12892764390087251114834094135881113029625174256248535119246116278891435001755L), (3, 32742630886892579331083790327379584614547769967814710811249454740219810823864L)]

#### Recovering from shares

    >>> points_to_secret_int(shares[0:2])
    88985120633792790105905686761572077713049967498756747774697023364147812997770L

### Custom formats

#### Splitting into shares

    >>> from pyseltongue import SecretSharer, base64_chars
    >>> sharer_class = SecretSharer
    >>> sharer_class.share_charset = base64_chars
    >>> shares = sharer_class.split_secret("c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a", 2, 3)
    ['B-JpxCTUQ9D+q93JglQM9yRinI2Cyxe92FTBSYa93ppfY', 'C-HAmR0pjHuHwL4rozXnFY05ysIJVqtf3pob1HCMaaZUm', 'D-EXbhV+1SYQ1Z6NxBfBM/YQ+PaP4j8B5N92X1pa9LJJ0']

#### Recovering from shares

    >>> sharer_class.recover_secret(shares[0:2])
    'c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a'
