"""630. Course Schedule III

There are n different online courses numbered from 1 to n. Each course has
some duration(course length) t and closed on dth day. A course should be
taken continuously for t days and must be finished before or on the dth day.
You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the
maximal number of courses that can be taken.

Example:

    Input:
        [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    Output:
        3
    Explanation:
        There're totally 4 courses, but you can take 3 courses at most:
        - First, take the 1st course, it costs 100 days so you will finish it
          on the 100th day, and ready to take the next course on the 101st day.
        - Second, take the 3rd course, it costs 1000 days so you will finish
          it on the 1100th day, and ready to take the next course on the
          1101st day.
        - Third, take the 2nd course, it costs 200 days so you will finish it
          on the 1300th day.
        - The 4th course cannot be taken now, since you will finish it on the
          3300th day, which exceeds the closed date.

Note:

    - The integer 1 <= d, t, n <= 10,000.
    - You can't take two courses simultaneously.

"""
import heapq


def schedule_course(courses):
    """
    :type courses: List[List[int]]
    :rtype: int
        """

        total_length = 0
        course_heap = []

        for course in courses:
            length, end_date = course
            total_length += length
            if total_length > end_date:
                if (len(course_heap) > 0 and
                        total_length + course_heap[0][0] < end_date):
                    total_length -= pop(course_heap)[0]
            push(course_heap, course)
        return len(course_heap)


def push(heap, course_item):
    length, end_date = course_item
    heapq.heappush(heap, (-length, end_date))
    return heap


def pop(heap):
    length, end_date = heapq.heappop(heap)
    return [-length, end_date]
