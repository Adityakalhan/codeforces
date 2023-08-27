#include<bits/stdc++.h>
using namespace std;
pair<int,int> get_row_col(vector<vector<int>> &matrix){
    for(int r = 0; r < 5 ; r++){
        for(int c= 0; c < 5;c++){
            if(matrix[r][c]==1){
                pair<int,int> p;
                p.first =r;
                p.second = c;
                return p; 
            }
        }
    }
}

int recursion(int r, int c, set<pair<int,int>> &visited, vector<vector<int>> &matrix) {
    
    if (r >= 5 || r < 0 || c >= 5 || c < 0) {
        return INT_MAX;
    }
    
    if (matrix[r][c] == 1 && r == 2 && c == 2) {
        return 0;
    }
    
    if (visited.find(make_pair(r,c)) != visited.end()) {
        return INT_MAX;
    }
    
    visited.insert(make_pair(r,c));
    
    int mini = INT_MAX;
    int dr[] = {-1, 1, 0, 0};  // delta row (up, down, left, right)
    int dc[] = {0, 0, -1, 1};  // delta col (up, down, left, right)
    
    for (int i = 0; i < 4; i++) {
        int newRow = r + dr[i];
        int newCol = c + dc[i];
        
        if (newRow >= 0 && newRow < 5 && newCol >= 0 && newCol < 5) {
            swap(matrix[r][c], matrix[newRow][newCol]);
            int temp = recursion(newRow, newCol, visited, matrix);
            if (temp != INT_MAX) {
                mini = min(mini, temp + 1);
            }
            swap(matrix[r][c], matrix[newRow][newCol]);
        }
    }
    
    visited.erase(make_pair(r,c));

    return mini;
}
vector<vector<int>> take_input(){
    vector<vector<int>> vect;
    for(int i = 0 ; i < 5; i++){
        vector<int> components;
        int temp;
        for(int j = 0; j < 5 ; j++){
            cin >> temp;
            components.push_back(temp);
        }
        vect.push_back(components);
    }

    return vect;
}
int main(){
    vector<vector<int>> matrix;
    pair<int,int> p;
    matrix = take_input();
    p = get_row_col(matrix);
    set<pair<int,int>> visited;
    cout<<recursion(p.first,p.second,visited,matrix);
}