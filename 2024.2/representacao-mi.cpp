#include <iostream>
#include <vector>
using namespace std;

typedef struct grafo{
  int n,m;
  vector<vector<int>> e;
}grafo;

grafo g;

void lerGrafo(){
  int i, n, m;
  
  cin >> n;
  g.n = n;
  
  cin >> m;
  g.m = m;
  
  g.e.resize(n);
  for(i=0;i<n;i++){
    g.e[i].resize(m,0);
  }
  
  int u,v;
  for(i=0;i<m;i++){
    cin >> u;
    cin >> v;
    g.e[u][i] = 1; g.e[v][i] = 1;
  }
}

void imprimeGrafo(){
  int i,j;
  for(i=0;i<g.n;i++){
    for(j=0;j<g.m;j++){
      cout << g.e[i][j] << " ";
    }
    cout << endl;
  }
}

int main()
{
    lerGrafo();
    imprimeGrafo();
    
    return 0;
}