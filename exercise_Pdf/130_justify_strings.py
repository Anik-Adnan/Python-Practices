# Python provides functions for justifying strings, enabling text padding to make aligning various strings much easier.
# Below is an example of str.ljust and str.rjust:

interstates_lengths = {
    5: (1381, 2222),
    19: (63, 102),
    40: (2555, 4112),
    93: (189, 305),
}
for road, length in interstates_lengths.items():
    miles, kms = length
    print('{} -> {} mi. ({} km.)'.format(str(road).rjust(4), str(miles).ljust(4),
                                         str(kms).ljust(4)))
# 40 -> 2555 mi. (4112 km.)
# 19 -> 63 mi. (102 km.)
# 5 -> 1381 mi. (2222 km.)
# 93 -> 189 mi. (305 km.)
