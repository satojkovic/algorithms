#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

bool check(ll n)
{
    string s = to_string(n);
    for (ll i = 0; i < s.size(); ++i) {
        if (s[i] == '4') {
            return false;
        } 
    }
    return true;
}

void bruteforce(ll t)
{
    ll N;
    cin >> N;

    for (ll i = 1; i < N; ++i) {
        ll A = i;
        ll B = N - A;
        if (check(A) && check(B)) {
            cout << "Case #" << t << ": " << A << " " << B << endl;
            break;
        }
    }

}

pair<string,string> decompose(string& A)
{
    string B = string(A.size(), '0');
    for (ll i = 0; i < A.size(); ++i) {
        if (A[i] == '4') {
            A[i] = '2';
            B[i] = '2';
        }
    }
    ll num_leading_zeros = 0;
    for (ll i = 0; i < B.size(); ++i) {
        if (B[i] != '0') break;
        num_leading_zeros++;
    }
    return pair<string, string>(A, B.substr(num_leading_zeros));
}

int main()
{
    ll T;
    cin >> T;
    for (ll t = 1; t < T + 1; ++t) {
        string N;
        cin >> N;
        pair<string, string> ret = decompose(N);
        cout << "Case #" << t << ": " << ret.first << " " << ret.second << endl;
    }
}
