#include <bits/stdc++.h>
using namespace std;

bool check_perfect(vector<int> &slice)
{
    int sum = accumulate(slice.begin(), slice.end(), 0);
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
                vector<int> slice;
                copy(arr.begin() + i, arr.begin() + j + 1, back_inserter(slice));
                if (check_perfect(slice))
                {
                    res++;
                }
            }
        }
        cout
            << "Case #" << t << ": " << res << endl;
    }
}
