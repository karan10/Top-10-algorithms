#include <iostream>
#include <ctime>
using namespace std;

int max(int a, int b) { return ( a > b ) ? a : b; }

// int get_max_revenue(int p[], int n)
// {
//     int val[n+1];
//     val[0] = 0;
//     int revenue;
//     if ( n == 0 )
//         return 0;
//     revenue = -999;
//     for (int i=0;i<n;i++)
//         revenue = max(revenue, p[i] + get_max_revenue(p, n-i-1));

//     return revenue;

// }


int get_max_revenue(int p[], int n, int val[])
{


    if (val[n] >= 0)
        return val[n];

    int revenue;
    if ( n == 0 )
        revenue = 0;
    else
    {    
        revenue = -999;
        for (int i=0;i<n;i++)
            revenue = max(revenue, p[i] + get_max_revenue(p, n-i-1, val));
    }

    val[n] = revenue;

    return revenue;

}

int main()
{

  
    int price[] = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30},n;
    cin>>n;

    int val[n+1];
    for (int i=0;i<n;i++)
        val[i] = -999;

    cout<<"output"<<endl;
    cout<<get_max_revenue(price, n, val)<<endl;
    // cout<<get_max_revenue(price, n)<<endl;

    cout<<"\n";


    return 0;
}
