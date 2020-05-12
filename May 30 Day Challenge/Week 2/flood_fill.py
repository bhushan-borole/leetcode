class Solution:
    def floodFill(self, image, sr, sc, newColor):
        rows = len(image)
        cols = len(image[0])
        orig_color = image[sr][sc]
        def flood(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or image[r][c] != orig_color:
                return
            image[r][c] = newColor
            flood(r+1, c)
            flood(r, c+1)
            flood(r-1, c)
            flood(r, c-1)
        
        if orig_color != newColor:
            flood(sr, sc)
        return image