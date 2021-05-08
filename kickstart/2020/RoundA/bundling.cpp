#include <bits/stdc++.h>

using namespace std;
typedef struct _TrieNode
{
    _TrieNode *child[26];
    int count = 0;
} TrieNode;

void insert(TrieNode *root, string &s)
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

int calc_score(TrieNode *root, int depth, int K)
{
    int curr_score = 0;
    for (int i = 0; i < 26; ++i)
    {
        if (root->child[i])
        {
            int score = calc_score(root->child[i], depth + 1, K);
            curr_score += score;
            root->count += root->child[i]->count;
        }
    }
    while (root->count >= K)
    {
        root->count -= K;
        curr_score += depth;
    }
    return curr_score;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        TrieNode *root = new TrieNode();
        int N, K;
        cin >>
            N >> K;
        string strings[N];
        for (int i = 0; i < N; ++i)
        {
            cin >> strings[i];
            insert(root, strings[i]);
        }
        int score = calc_score(root, 0, K);
        cout
            << "Case #" << t << ": " << score << endl;
        delete root;
    }
    return 0;
}
