from typing import Dict, List, Optional
from collections import defaultdict, deque


def solution(courses: Dict[str, List[str]]) -> Optional[List[str]]:
    indeg = defaultdict(int)
    for course in courses:
        for sub_course in courses[course]:
            indeg[sub_course] += 1
    stack = deque([course for course in courses if indeg[course] == 0])
    res = []
    while stack:
        course = stack.popleft()
        res.append(course)
        for sub_course in courses[course]:
            indeg[sub_course] -= 1
            if indeg[sub_course] == 0:
                stack.append(sub_course)
    if len(res) == len(courses):
        return res[::-1]
    return None
