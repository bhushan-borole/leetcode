class Solution:
    def checkStraightLine(self, coordinates):
        if len(coordinates) == 2:
            return True

        p1, p2 = coordinates[0], coordinates[1]

        return all(p1[0] * p3[1] - p3[0] * p1[1] +
                p3[0] * p2[1] - p2[0] * p3[1] +
                p2[0] * p1[1] - p1[0] * p2[1] == 0
                for p3 in coordinates)