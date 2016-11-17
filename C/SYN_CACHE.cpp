#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
//#include <stdbool.h>

int SIZE = 20;
struct DataItem* hashArray[20];

struct DataItem
{
	int data;
	int key;
};


struct DataItem* dummyItem;
struct DataItem* item;

int hashCode(int key)
{
	return key % SIZE;
}

struct DataItem *search(int key)
{
	//get the hash 
	int hashIndex = hashCode(key);

	//move in array until an empty 
	while (hashArray[hashIndex] != NULL)
	{

		if (hashArray[hashIndex]->key == key)
			return hashArray[hashIndex];

		//go to next cell
		++hashIndex;

		//wrap around the table
		hashIndex %= SIZE;
	}

	return NULL;
}

void insert(int key, int data)
{

	struct DataItem *item = (struct DataItem*) malloc(sizeof(struct DataItem));
	item->data = data;
	item->key = key;

	//get the hash 
	int hashIndex = hashCode(key);

	//move in array until an empty or deleted cell
	while (hashArray[hashIndex] != NULL && hashArray[hashIndex]->key != -1) {
		//go to next cell
		++hashIndex;

		//wrap around the table
		hashIndex %= SIZE;
	}

	hashArray[hashIndex] = item;
}

struct DataItem* remove(struct DataItem* item)
{
	int key = item->key;

	//get the hash 
	int hashIndex = hashCode(key);

	//move in array until an empty
	while (hashArray[hashIndex] != NULL) {

		if (hashArray[hashIndex]->key == key) {
			struct DataItem* temp = hashArray[hashIndex];

			//assign a dummy item at deleted position
			hashArray[hashIndex] = dummyItem;
			return temp;
		}

		//go to next cell
		++hashIndex;

		//wrap around the table
		hashIndex %= SIZE;
	}

	return NULL;
}

void display() {
	int i = 0;

	for (i = 0; i<SIZE; i++) {

		if (hashArray[i] != NULL)
			printf(" (%d,%d)", hashArray[i]->key, hashArray[i]->data);
		else
			printf(" ~~ ");
	}

	printf("\n");
}

int main() {
	dummyItem = (struct DataItem*) malloc(sizeof(struct DataItem));
	dummyItem->data = -1;
	dummyItem->key = -1;
	int tKey = 0, tData = 0, aSize = 0;
	char act = 't';
	
	while (act != 'X')
	{
		printf("\nEnter Desired Action: (A - Add Item to Table, D - Display Table, R - Remove Item from Table, S - Search Table by Key, X - Exit Program\n");
		scanf("%c", &act);
		switch (toupper(act))
		{
			case 'A':
				aSize++;
				printf("Please enter Key value:");
				scanf("%d", &tKey);
				printf("Please enter Data value:");
				scanf("%d", &tData);
				insert(tKey, tData);
				printf("\nItem Added\n");
				break;
			case 'D':
				display();
				break;
			case 'R':
				aSize--;
				printf("Please enter Key value:\n");
				scanf("%d", &tKey);
				item = search(tKey);
				remove(item);
				printf("Item Added\n");
				break;
			case 'S':
				printf("Please enter Key value:\n");
				scanf("%d", &tKey);
				item = search(tKey);
				printf("Key Value: %d - Data Value: %d\n", item->key, item->data);
				break;
			case 'X':
				break;
		}
	}
}
