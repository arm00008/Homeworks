# 12.Line Segment Intersection
# You are given four real numbers- a1, b1, a2, b2 - The endpoints of two
# line segments on a line. Find the length of their intersection. Note that the
# order of the endpoints of a segment is irrelevant, i.e. the segments [1;2]
# and [2;1] are considered the same.

def intersection_length(a1, b1, a2, b2):
    segment1 = sorted([a1, b1])
    segment2 = sorted([a2, b2])

    start_point = max(segment1[0], segment2[0])
    end_point = min(segment1[1], segment2[1])

    length = max(0, end_point - start_point)

    return length


a1, b1 = map(float, input("Enter the endpoints of the first line segment (a1 b1): ").split())
a2, b2 = map(float, input("Enter the endpoints of the second line segment (a2 b2): ").split())

# Calculate and print the length of the intersection
intersection_length_result = intersection_length(a1, b1, a2, b2)
print("Length of the intersection:", intersection_length_result)
