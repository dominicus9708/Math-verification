#include <bits/stdc++.h>
using namespace std;
using u64=uint64_t;using u128=unsigned __int128;
void print128(u128 x){if(!x){cout<<0;return;}string s;while(x){s.push_back(char('0'+x%10));x/=10;}reverse(s.begin(),s.end());cout<<s;}
int main(int argc,char**argv){if(argc<2){cerr<<"usage: certificate CHUNK [allow27.bin]\n";return 1;}int chunk=atoi(argv[1]);if(chunk<0||chunk>=16)return 2;const string bitpath=argc>2?argv[2]:"allow27.bin";const int L=27;const u64 RMASK=(1ULL<<27)-1;const u64 CH=1ULL<<28;const u64 start=u64(chunk)*CH;const u64 end=start+CH;
vector<u64>bits(1ULL<<21);ifstream f(bitpath,ios::binary);f.read(reinterpret_cast<char*>(bits.data()),bits.size()*sizeof(u64));if(!f){cerr<<"cannot read retained-residue bitset\n";return 3;}
vector<u128>p3(45,1);for(int i=1;i<=44;i++)p3[i]=p3[i-1]*3;const u128 Nmin=4*(p3[44]+p3[32])+3;u64 m44=1,m32=1;for(int i=0;i<44;i++)m44=(m44*3)&RMASK;for(int i=0;i<32;i++)m32=(m32*3)&RMASK;const u64 nmod=(4*((m44+m32)&RMASK)+3)&RMASK;
u64 g=start^(start>>1),prevg=g;u128 sum=0;for(int i=0;i<32;i++)if((g>>i)&1ULL)sum+=p3[i];u64 removed=0,fringe=0,failures=0;int max_tau=0;u128 max_start=0;
for(u64 k=start;k<end;k++){if(k>start){g=k^(k>>1);u64 diff=g^prevg;int b=__builtin_ctzll(diff);if((g>>b)&1ULL)sum+=p3[b];else sum-=p3[b];prevg=g;}u64 r=(nmod+4*u64(sum&RMASK))&RMASK;if(!((bits[r>>6]>>(r&63))&1ULL)){++removed;continue;}++fringe;u128 n=Nmin+4*sum,x=n;bool ok=false;int tau=0;for(int step=1;step<=5000;step++){if(x&1)x=(3*x+1)/2;else x/=2;if(x<n){ok=true;tau=step;break;}}if(!ok)++failures;if(tau>max_tau){max_tau=tau;max_start=n;}}
static const u64 exp_removed[16]={259947187,259940679,259939506,259943766,259941282,259941612,259945101,259941254,259943964,259944407,259940336,259947067,259943744,259945142,259944929,259946018};
static const u64 exp_fringe[16]={8488269,8494777,8495950,8491690,8494174,8493844,8490355,8494202,8491492,8491049,8495120,8488389,8491712,8490314,8490527,8489438};
static const int exp_maxtau[16]={444,470,406,403,465,360,425,433,463,424,405,460,413,365,373,425};
cout<<"chunk "<<chunk<<" removed "<<removed<<" fringe "<<fringe<<" failures "<<failures<<" max_tau "<<max_tau<<" max_start ";print128(max_start);cout<<"\n";
if(removed!=exp_removed[chunk]||fringe!=exp_fringe[chunk]||failures!=0||max_tau!=exp_maxtau[chunk]){cerr<<"certificate mismatch\n";return 4;}return 0;}
