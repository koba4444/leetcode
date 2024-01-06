import bisect


class MyCalendarThree:

    def __init__(self):
        self.booking_number = 0
        self.left = []
        self.right = []
        self.maxbooking = 0
        self.a = [None] * 3200


    def book(self, start: int, end: int) -> int:

        def a_build(self.a):

        def a_update(self.a, start, end):




        left_pretends = bisect.bisect_right(self.left, start, key=lambda x: x[1])
        right_pretends = bisect.bisect_right(self.right, start, key=lambda x: x[1])
        set1 = set([x[0] for x in self.left[:left_pretends]])
        set2 = set([x[0] for x in self.right[right_pretends:]])
        start_inclusion_set = set1 & set2

        if left_pretends >= 1 and right_pretends< len(self.right):
            print(start, end, self.left[left_pretends-1], self.right[right_pretends], start_inclusion_set)
        left_pretends = bisect.bisect_left(self.left, end, key=lambda x: x[1])
        right_pretends = bisect.bisect_left(self.right, end, key=lambda x: x[1])
        set1 = set([x[0] for x in self.left[:left_pretends]])
        set2 = set([x[0] for x in self.right[right_pretends:]])
        end_inclusion_set = set1 & set2
        if left_pretends >= 1 and right_pretends < len(self.right):
            print(start, end, self.left[left_pretends-1], self.right[right_pretends], end_inclusion_set)



        left_pretends = bisect.bisect_right(self.left, start, key=lambda x: x[1])
        right_pretends = bisect.bisect_left(self.right, end, key=lambda x: x[1])
        set1 = set([x[0] for x in self.left[left_pretends:]])
        set2 = set([x[0] for x in self.right[:right_pretends]])
        wider_inclusion_set = set1 & set2
        print(start, end, self.left, self.right, wider_inclusion_set)

        self.booking_number += 1
        self.left.append([self.booking_number, start])
        self.left.sort(key=lambda x: x[1])
        self.right.append([self.booking_number, end])
        self.right.sort(key=lambda x: x[1])
        if len(self.left) == 1:
            self.maxbooking = 1
            return self.maxbooking
        else:
            m = max(len(start_inclusion_set), len(end_inclusion_set)) + len(wider_inclusion_set)
        self.maxbooking = max(self.maxbooking, m + 1)
        return self.maxbooking

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
b = MyCalendarThree()
print(b.book(10, 20))
#print(b.book(9, 21))
#print(b.book(8, 22))
#print(b.book(7, 23))






print(b.book(50,60))
print(b.book(10,40))
print(b.book(5, 15))
print(b.book(5, 10))
print(b.book(25,55))
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]