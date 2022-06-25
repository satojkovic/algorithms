#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

void print(const vector<int> &data)
{
    for (int i = 0; i < data.size(); ++i)
    {
        cout << data[i];
        if (i == data.size() - 1)
            cout << endl;
        else
            cout << ",";
    }
}

void partition(vector<int> &data, int l, int r)
{
    int m = l;
    for (int i = l + 1; i <= r; ++i)
    {
        if (data[i] < data[l])
            swap(data[i], data[++m]);
    }
    swap(data[l], data[m]);
}

int main()
{
    vector<int> data{55, 41, 59, 26, 53, 58, 97, 93};
    partition(data, 0, data.size() - 1);
    print(data);
}
