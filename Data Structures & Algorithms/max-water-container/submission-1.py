class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            length = r - l
            if heights[l] > heights[r]:
                height = heights[r]
                new_area = length * height
                area = max(area, new_area)
                r -= 1
            elif heights[l] < heights[r]:
                height = heights[l]
                new_area = length * height
                area = max(area, new_area)
                l += 1
            else:
                area = max(area, length * heights[l])

                l_next = l + 1
                if l_next < r:
                    height_1 = min(heights[l_next], heights[r])
                    length1 = r - l_next
                    new_area1 = height_1 * length1
                    area = max(area, new_area1)

                r_next = r - 1
                if l < r_next:
                    length2 = r_next - l
                    height2 = min(heights[l], heights[r_next])
                    area = max(area, length2 * height2) 
                
                l += 1
                r -= 1

                
        return area
        


        