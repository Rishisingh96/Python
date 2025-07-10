#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int adj[MAX][MAX];     // Adjacency matrix
int visited[MAX];      // Visited array
int queue[MAX];        // Queue for BFS
int front = -1, rear = -1;

// Function to add edge in the graph (undirected)
void addEdge(int u, int v) {
    adj[u][v] = 1;
    adj[v][u] = 1; // For undirected graph
}

// ------------------- DFS ----------------------
void DFS(int vertex, int n) {
    visited[vertex] = 1;
    printf("%d ", vertex);

    for (int i = 0; i < n; i++) {
        if (adj[vertex][i] == 1 && !visited[i])
            DFS(i, n);
    }
}

// ------------------- BFS ----------------------
void enqueue(int value) {
    if (rear == MAX - 1)
        return;
    if (front == -1)
        front = 0;
    rear++;
    queue[rear] = value;
}

int dequeue() {
    if (front == -1 || front > rear)
        return -1;
    return queue[front++];
}

void BFS(int start, int n) {
    for (int i = 0; i < n; i++)
        visited[i] = 0;

    enqueue(start);
    visited[start] = 1;

    while (front <= rear) {
        int current = dequeue();
        printf("%d ", current);

        for (int i = 0; i < n; i++) {
            if (adj[current][i] == 1 && !visited[i]) {
                enqueue(i);
                visited[i] = 1;
            }
        }
    }
}

// ------------------ Main -----------------------
int main() {
    int n, e, u, v, start;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter number of edges: ");
    scanf("%d", &e);

    printf("Enter edges (u v):\n");
    for (int i = 0; i < e; i++) {
        scanf("%d %d", &u, &v);
        addEdge(u, v);
    }

    printf("Enter starting vertex for DFS: ");
    scanf("%d", &start);

    for (int i = 0; i < n; i++)
        visited[i] = 0;

    printf("DFS Traversal: ");
    DFS(start, n);

    printf("\nEnter starting vertex for BFS: ");
    scanf("%d", &start);

    printf("BFS Traversal: ");
    BFS(start, n);

    return 0;
}
