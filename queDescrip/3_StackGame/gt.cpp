#include<bits/stdc++.h>
#define mp make_pair
#define f first
#define se second
#define pb push_back
#define ms memset
#define MOD 1000000007
#define sp fixed<<setprecision
#define sz sizeof
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
bool pr[1000007];
void sieve(){pr[0]=1;pr[1]=1;for(int i=2;i*i<(1000007);i++){for(int j=2*i;j<=1000007;j+=i){pr[j]=1;}}}
ll fpow(ll x,ll y){x=x%MOD;ll res=1;while(y){if(y&1)res=res*x;res%=MOD;y=y>>1;x=x*x;x%=MOD;}return res;}
ll hcf(ll n1, ll n2)
{
    if (n2 != 0)
       return hcf(n2, n1%n2);
    else 
       return n1;
}
int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0); 
	ll t,n;
	cin>>t;
	while(t--)
	{
		cin>>n;
		map<ll,ll>m;
		map<ll,ll>::iterator it;
		for(int i=0;i<n;i++)
		{
			ll x;
			cin>>x;
			m[x]++;		
		}
		bool ok=false;
		for(it=m.begin();it!=m.end();it++)
		{
			if((it->second)%2==1)
			{
				ok=true;
				break;
			}

		}
                if(ok)
		cout<<"Darshan\n";
		else
		cout<<"Shubham\n";
		
	}
}
