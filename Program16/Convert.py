from typing import ByteString


def Convert(ch) :
    if (ch >= 'A') & (ch <= 'Z') :
        ch1 = bytes(ch) + 32

        print(ch1)