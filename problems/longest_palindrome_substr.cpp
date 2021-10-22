#include <bits/stdc++.h>

using namespace std;

bool check(const string &s, const vector<vector<int>> &dp, const int i, const int j)
{
    if (i == j)
    {
        return true;
    }
    else if (i + 1 == j)
    {
        return s[i] == s[j];
    }
    else
    {
        return dp[i + 1][j - 1] && s[i] == s[j];
    }
}

string longest_palindrome(const string s)
{
    int n = s.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int i = 0; i < n; ++i)
    {
        dp[i][i] = 1;
    }

    int max_start_pos = 0;
    int max_len = 1;
    for (int i = n - 1; i >= 0; --i)
    {
        for (int j = i; j < n; ++j)
        {
            if (check(s, dp, i, j))
            {
                dp[i][j] = 1;
                int cand_len = j - i + 1;
                if (cand_len > max_len)
                {
                    max_len = cand_len;
                    max_start_pos = i;
                }
            }
        }
    }
    return s.substr(max_start_pos, max_len);
}

int main()
{
    string s;
    cin >> s;
    string ret = longest_palindrome(s);
    cout << ret << endl;
    return 0;
}
