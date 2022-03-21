#include <bits/stdc++.h>

using namespace std;

int which_digit_to_insert(string &s)
{
    int sum = 0;
    for (int i = 0; i < s.size(); ++i)
    {
        sum += int(s[i] - '0');
    }
    if (sum % 9 != 0)
    {
        return 9 - sum % 9;
    }
    else
    {
        return 0;
    }
}

vector<int> get_digits(string &s, int L)
{
    vector<int> digits;
    for (int i = 0; i < L; ++i)
    {
        digits.push_back(int(s[i] - '0'));
    }
    return digits;
}

int where_to_insert(string &s, int d)
{
    int k = 0;
    int L = s.size();
    vector<int> digits = get_digits(s, L);
    for (int i = 0; i < L; ++i)
    {
        if (digits[i] > d)
        {
            k = L - i;
            break;
        }
    }
    if (d == 0 && k == L)
    {
        k -= 1;
    }
    return k;
}

string insert_digit_str(string &s, int d, int k)
{
    string before = s.substr(0, s.size() - k);
    string after = s.substr(s.size() - k);
    return before + to_string(d) + after;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t < T + 1; ++t)
    {
        string s;
        cin >> s;
        int d = which_digit_to_insert(s);
        int k = where_to_insert(s, d);
        cout << "Case #" << t << ": " << insert_digit_str(s, d, k) << endl;
    }
}
