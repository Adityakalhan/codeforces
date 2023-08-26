#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> take_input(){
    vector<vector<int>> vect;
    int n;
    cin >> n;
    for(int i = 0 ; i < n ; i++){
        vector<int> components;
        int temp;
        for(int j = 0; j < 3 ; j++){
            cin >> temp;
            components.push_back(temp);
        }
        vect.push_back(components);
    }

    return vect;
}
int main(){
    vector<vector<int>> vectors = take_input();
    int x_comp = 0,y_comp = 0,z_comp = 0;
    for(int i = 0 ; i < vectors.size() ; i++){
        int x = vectors[i][0];
        int y = vectors[i][1];
        int z = vectors[i][2];

        x_comp += x;
        y_comp += y;
        z_comp += z;
    }

    if(x_comp == 0 && y_comp == 0 && z_comp == 0){
        cout << "YES";
    }
    else {
        cout << "NO";
    }
    return 0;
}