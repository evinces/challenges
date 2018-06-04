"""RGB To Hex Conversion

The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

"""


def rgb(r, g, b):
    r, g, b = min(max(r, 0), 255), min(max(g, 0), 255), min(max(b, 0), 255)
    return (dec_to_hex[r / 16] + dec_to_hex[r % 16] +
            dec_to_hex[g / 16] + dec_to_hex[g % 16] +
            dec_to_hex[b / 16] + dec_to_hex[b % 16])


dec_to_hex = {
    0: "0", 1: "1",  2: "2",  3: "3",  4: "4",  5: "5",  6: "6",  7: "7",
    8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
}
