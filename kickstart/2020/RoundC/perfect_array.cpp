#include <bits/stdc++.h>
typedef long long ll;
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
    ll T, N;
    cin >> T;
    for (ll t = 1; t <= T; ++t)
    {
        cin >> N;
        vector<ll> arr;
        for (ll i = 0; i < N; ++i)
        {
            int d;
            cin >> d;
            arr.push_back(d);
        }
        ll res = 0;
        ll sum = 0;
        ll min_sum = 0;
        unordered_map<ll, ll> m;
        m[0] = 1;
        for (ll i = 0; i < arr.size(); ++i)
        {
            sum += arr[i];
            min_sum = min(sum, min_sum);
            for (ll j = 0; sum - (j * j) >= min_sum; ++j)
            {
                if (m.count(sum - (j * j)) == 1)
                {
                    res += m[sum - (j * j)];
                }
            }
            m[sum] += 1;
        }
        cout
            << "Case #" << t << ": " << res << endl;
    }
}
