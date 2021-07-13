#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t < T + 1; ++t)
    {
        int N, K;
        cin >> N >> K;
        vector<int> arr;
        for (int i = 0; i < N; ++i)
        {
            int x;
            cin >> x;
            arr.push_back(x);
        }

        int res = 0;
        int dc = 0;
        for (int i = 1; i < N; ++i)
        {
            if (arr[i] == arr[i - 1] - 1)
            {
                dc++;
            }
            else
            {
                dc = 0;
            }
            if (arr[i] == 1 && dc >= K - 1)
            {
                res++;
            }
        }
        cout << "Case #" << t << ": " << res << endl;
    }
}
