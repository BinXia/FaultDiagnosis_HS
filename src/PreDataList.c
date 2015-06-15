
// 構建鏈表結構
struct node
{  
    double num;  
    struct node *next;
}Node;
typedef struct node *DNode;



int create(DNode *head, int size, double value)
{
	DNode p = NULL;
	int i;

	*head = (DNode)malloc(sizeof(Node));
	(*head)->next = NULL;

	for (int i = 0; i < size; ++i){
		p = (DNode)malloc(sizeof(Node));
		p->num = value;
		p->next = (*head)->next;
		(*head)->next = p;
	}
	return 1;
}