#include <bits/stdc++.h>
using namespace std;

bool check_perfect(vector<int> &arr, int start, int end)
{
    int sum = accumulate(arr.begin() + start, arr.begin() + end + 1, 0);
    if (sum >= 0)
    {
        float sq = sqrt(float(sum));
        return (sq - floor(sq)) == 0;
    }
    return false;
}

void print_vector(vector<int> &v)
{
    for (int i = 0; i < v.size(); ++i)
    {
        cout << v[i];
        if (i != v.size() - 1)
        {
            cout << ',';
        }
    }
    cout << endl;
}

int main()
{
    int T, N;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> N;
        vector<int> arr;
        for (int i = 0; i < N; ++i)
        {
            int d;
            cin >> d;
            arr.push_back(d);
        }
        int res = 0;
        for (int i = 0; i < N; ++i)
        {
            for (int j = i; j < N; ++j)
            {
                if (check_perfect(arr, i, j))
                {
                    res++;
                }
            }
        }
        cout
            << "Case #" << t << ": " << res << endl;
    }
}
