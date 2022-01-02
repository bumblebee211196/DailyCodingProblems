class Trie:
    def __init__(self, val="*"):
        self.val = val
        self.children = []
        self.is_valid_word = False

    def add(self, word):
        curr_node = self
        for char in word:
            node = Trie(char)
            if len(curr_node.children) > 0:
                for child in curr_node.children:
                    if char == child.val:
                        curr_node = child
                        break
                else:
                    curr_node.children.append(node)
                    curr_node = node
            else:
                curr_node.children.append(node)
                curr_node = node
        curr_node.is_valid_word = True

    def get_matching_words(self, prefix):
        curr_node = self
        for char in prefix:
            for child in curr_node.children:
                if child.val == char:
                    curr_node = child
                    break
            else:
                return []
        word_list = [f"{prefix}{curr_node.val}"] if curr_node.is_valid_word else []
        child_list = [(curr_node, prefix)]
        while len(child_list) > 0:
            curr_node, prefix = child_list.pop(0)
            for child in curr_node.children:
                if child.is_valid_word:
                    word_list.append(f"{prefix}{child.val}")
                child_list.append((child, f"{prefix}{child.val}"))
        return word_list


def solution(s, query_strings):
    trie = Trie()
    for word in query_strings:
        trie.add(word)
    return trie.get_matching_words(s)


assert solution("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
assert solution("ca", ["cat", "car", "cer"]) == ["cat", "car"]
assert solution("ae", ["cat", "car", "cer"]) == []
assert solution("ae", []) == []
