#include <iostream>
#include <vector>
using namespace std;

typedef struct noAresta{
  int v;
  noAresta *prox;
}noAresta;

typedef struct grafo{
  int n,m;
  vector<noAresta*> l;
}grafo;

grafo g;

void insere(int u, int v){
  noAresta *p;
  p = g.l[u];
  g.l[u] = new noAresta;
  g.l[u]->v = v;
  g.l[u]->prox = p;
}

void lerGrafo(){
  int i, n, m;
  
  cin >> n;
  g.n = n;
  
  cin >> m;
  g.m = m;
  
  g.l.resize(n);
  for(i=0;i<n;i++){
    g.l[i] = NULL;
  }
  
  int u,v;
  for(i=0;i<m;i++){
    cin >> u;
    cin >> v;
    insere(u,v);
    insere(v,u);
  }
}



void imprimeGrafo(){
  int i,j;
  noAresta *p;
  for(i=0;i<g.n;i++){
    p = g.l[i];
    cout << i << ": ";
    while(p!=NULL){
      cout << p->v << " ";
      p = p->prox;
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