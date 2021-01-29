def solution(file_path):
    if '.' not in file_path:
        return 0
    lvl = {-1: 0}
    max_len = 0
    for line in file_path.split('\n'):
        depth = line.count('\t')
        if depth in lvl:
            lvl[depth] = max(lvl[depth], len(line) - depth + lvl[depth - 1])
        else:
            lvl[depth] = len(line) - depth + lvl[depth - 1]
        if '.' in line:
            max_len = max(max_len, lvl[depth] + depth)
    return max_len


assert solution('dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext') == 20
assert solution('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext') == 32
