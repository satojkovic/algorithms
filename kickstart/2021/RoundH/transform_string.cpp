#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    cin >> T;
    string letters = "abcdefghijklmnopqrstuvwxyz";
    int len_letters = static_cast<int>(letters.size());
    for (int t = 1; t <= T; ++t)
    {
        string S, F;
        cin >> S;
        cin >> F;
        vector<vector<int>> dist;
        dist.resize(F.size());
        for (int i = 0; i < F.size(); ++i)
        {
            int af = F[i];
            for (int j = 0; j < S.size(); ++j)
            {
                int as = S[j];
                dist[i].push_back(min(abs(af - as), len_letters - abs(af - as)));
            }
        }
        int res = 0;
        for (int i = 0; i < S.size(); ++i)
        {
            int min_dist = len_letters;
            for (int j = 0; j < F.size(); ++j)
            {
                if (min_dist > dist[j][i])
                {
                    min_dist = dist[j][i];
                }
            }
            res += min_dist;
        }
        cout << "Case #" << t << ": " << res << endl;
    }
}
