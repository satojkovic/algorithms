#include <iostream>
#include <string>
#include <utility>

typedef struct _TrieNode
{
    _TrieNode *child[26];
    int count = 0;
} TrieNode;

void insert(TrieNode *root, std::string &s)
{
    TrieNode *curr = root;
    for (int i = 0; i < s.size(); ++i)
    {
        int idx = s[i] - 'A';
        if (!curr->child[idx])
        {
            curr->child[idx] = new TrieNode();
        }
        curr = curr->child[idx];
    }
    curr->count++;
}

std::pair<int, int> calc_score(TrieNode *root, int depth, int K)
{
    int curr_score = 0;
    int curr_count = 0;
    for (int i = 0; i < 26; ++i)
    {
        if (root->child[i])
        {
            std::pair<int, int> score_count = calc_score(root->child[i], depth + 1, K);
            curr_score += score_count.first;
            curr_count += score_count.second;
        }
    }
    curr_count += root->count;
    while (curr_count >= K)
    {
        curr_count -= K;
        curr_score += depth;
    }
    return std::make_pair(curr_score, curr_count);
}

int main()
{
    int T = 0;
    std::cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        TrieNode *root = new TrieNode();
        int N = 0;
        int K = 0;
        std::string strings[N];
        std::cin >>
            N >> K;
        for (int i = 0; i < N; ++i)
        {
            std::cin >> strings[i];
            insert(root, strings[i]);
        }
        std::pair<int, int> score_count = calc_score(root, 0, K);
        std::cout
            << "Case #" << t << ": " << score_count.first << std::endl;
        delete root;
    }
}
