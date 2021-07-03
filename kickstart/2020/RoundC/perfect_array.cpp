#include <bits/stdc++.h>
using namespace std;

bool check_perfect(int sum)
{
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

vector<int> cumulative_sum(vector<int> &arr)
{
    vector<int> cum_sum;
    cum_sum.resize(arr.size() + 1);
    cum_sum[0] = 0;
    for (int i = 0; i < arr.size(); ++i)
    {
        cum_sum[i + 1] = cum_sum[i] + arr[i];
    }
    return cum_sum;
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
        vector<int> cum_sum = cumulative_sum(arr);
        int res = 0;
        for (int i = 0; i < N; ++i)
        {
            for (int j = i; j < N; ++j)
            {
                int sum = cum_sum[j + 1] - cum_sum[i];
                if (check_perfect(sum))
                {
                    res++;
                }
            }
        }
        cout
            << "Case #" << t << ": " << res << endl;
    }
}
