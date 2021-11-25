#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        string S;
        int K;
        cin >> S >> K;

        int N = static_cast<int>(S.size());
        int res = 0;
        for (int i = 0; i < N - K + 1; ++i)
        {
            if (S[i] == '-')
            {
                for (int k = 0; k < K; ++k)
                {
                    S[i + k] = S[i + k] == '-' ? '+' : '-';
                }
                res++;
            }
        }
        string cond;
        for (auto c : S)
        {
            if (c == '-')
            {
                cond = "IMPOSSIBLE";
                break;
            }
        }
        if (cond == "IMPOSSIBLE")
        {
            cout << "Case #" << t << ": " << cond << endl;
        }
        else
        {
            cout << "Case #" << t << ": " << res << endl;
        }
    }
}
