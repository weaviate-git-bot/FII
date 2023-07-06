#include <exception>
#include <iostream>
using namespace std;

class Exception
{
	const char* msg;
public:
	Exception(const char* s)
	{
		msg = s;
	}
	const char* GetMsg(){ return msg; }
};

class Compare
{
public:
	virtual int CompareElements(void* e1, void* e2) = 0;
};

template<class T>
class ArrayIterator
{
private:
	int Current; // mai adaugati si alte date si functii necesare pentru iterator
	int size;
	T* val;
public:
	ArrayIterator(T* val,int size)
	{
		this->val = val;
		this->Current=0;
		this->size=size;
	}

	ArrayIterator& operator ++ ()
	{
		this->val+=sizeof(T*);
		this->Current++;
		return *this;
	}
	ArrayIterator& operator -- ()
	{
		if(this->Current<=0)
			throw Exception("Index out of bounds");
		this->val--;
		this->Current--;
	}

	bool operator==(ArrayIterator<T> &tmp)
	{
		return this->size==this->Current;
	}
	bool operator!=(ArrayIterator<T> &tmp)
	{
		return this->val!=tmp.val;
	}

	T* GetElement()
	{
		return this->val;
	}
	T* operator*()
	{
		return this->val;
	}


};

template<class T>
class Array
{
private:
	T** List; // lista cu pointeri la obiecte de tipul T*
	int Capacity; // dimensiunea listei de pointeri
	int Size; // cate elemente sunt in lista

	void reallocateSize(int minSize=0)
	{
		do{
			this->Capacity*=2;
		}while(this->Capacity<minSize);
		
		T** tmp = (T**)realloc(this->List,this->Capacity*sizeof(T*));
		if(tmp == NULL)
			throw Exception("There is no memory left!");
		for(int i=this->Size;i<this->Capacity;i++)
			tmp[i] = new T;
		this->List = tmp;
	}
public:

	Array() // Lista nu e alocata, Capacity si Size = 0
	{
        this->Capacity=0;
        this->Size=0;
    }
    ~Array() // destructor
    {
		for(int i=0;i<this->GetSize();i++)
			delete this->List[i];
        delete[] this->List;
    }
	Array(int capacity) // Lista e alocata cu 'capacity' elemente
	{
        this->Capacity=capacity;
        this->List = new T*[this->Capacity];
        for(int i=0;i<this->Capacity;i++)
            this->List[i]= new T;
        this->Size = 0;
    }
	 // constructor de copiere
    Array(const Array<T> &otherArray)
	{
		this->Size = otherArray.GetSize();
		this->Capacity = otherArray.GetCapacity();
		this->List = new T*[this->Capacity];
		for(int i=0;i<this->Capacity;i++)
		{
			this->List[i] = new T;
			this->List[i] = otherArray[i];
		}
			
	}

	// arunca exceptie daca index este out of range
	T& operator[] (int index) const
    {
        if(index>this->Size || index<0)
            throw Exception("Index out of bounds");
        return *this->List[index];
    }

	// adauga un element de tipul T la sfarsitul listei si returneaza this
	const Array<T>& operator+=(const T &newElem) 
    {
        if(this->Size>=this->Capacity)
			this->reallocateSize();
        *this->List[this->Size++]= newElem;
        return *this;
    }

	void operator=(const Array<T>& otherArray)
	{
		int oSize = otherArray.GetSize();
		if(!oSize)
			throw Exception("Cannot copy an empty list!");
		if(oSize!=this->Capacity)
			this->reallocateSize(oSize);
		for(int i=0;i<oSize;i++)
			*this->List[i]=otherArray[i];
		this->Size=oSize;
	}
	// adauga un element pe pozitia index, retureaza this. Daca index e invalid arunca o exceptie
	const Array<T>& Insert(int index, const T &newElem) 
	{
		if(index>this->Size || index<0 || index>this->Capacity)
			throw Exception("Index out of bounds");
		*List[index]=newElem;
		return *this;
    }
	
	// sterge un element de pe pozitia index, returneaza this. Daca index e invalid arunca o exceptie
	const Array<T>& Delete(int index)
	{
		if(index>this->Size || index<0)
			throw Exception("Index out of bounds");
		for(int i=index;i<this->Size-1;i++)
		{
			this->List[i] = this->List[i+1];
		}
		this->List[this->Size]=0;
		this->Size--;
		return *this;
	}


	//default compare
	static int default_comparator(const T& v1, const T& v2)
	{
		return (v1>v2) ? 1 : 0;
	}

	// sorteaza folosind comparatia intre elementele din T
	void Sort()
	{
		this->Sort(default_comparator);
	} 
	// sorteaza folosind o functie de comparatie
	void Sort(int(*compare)(const T&, const T&))
	{

		for(int i=0;i<this->GetSize()-1;i++)
			for(int j=i+1;j<this->GetSize();j++)
				if(compare(*this->List[i], *this->List[j]))
				{
					swap(this->List[i], this->List[j]);
				}
	}; 
	 // sorteaza folosind un obiect de comparatie
	void Sort(Compare *comparator)
	{
		this->Sort(comparator->CompareElements);
	}

	// functii de cautare - returneaza pozitia elementului sau -1 daca nu exista
	// cauta un element folosind binary search in Array
	int BinarySearch(const T& elem)
	{
		return this->BinarySearch(elem, default_comparator);
	} 
	//  cauta un element folosind binary search si o functie de comparatie
	int BinarySearch(const T& elem, int(*compare)(const T&, const T&))
	{
		int left = 0, right=this->GetSize();
		while(left<=right)
		{
			int mij = (left+right)/2;
			if(*this->List[mij]==elem)
				return mij;
			if(compare(*this->List[mij],elem))
				right = mij-1;
			else 
				left = mij+1;
		}
		throw Exception("Element isn't in list!");
	}
	//  cauta un element folosind binary search si un comparator
	int BinarySearch(const T& elem, Compare *comparator)
	{
		return this->BinarySearch(elem,comparator->CompareElements);
	}

	// cauta un element in Array
	int Find(const T& elem)
	{
		return this->Find(elem, default_comparator);
	} 
	//  cauta un element folosind o functie de comparatie
	int Find(const T& elem, int(*compare)(const T&, const T&))
	{
		for(int i=0;i<this->GetSize();i++)
		{
			if(compare(*this->List[i], elem))
				return i;
		}
		throw Exception("Element isn't in list!");
	}
	//  cauta un element folosind un comparator
	int Find(const T& elem, Compare *comparator)
	{
		return this->Find(elem, comparator->CompareElements);
	}

	void Print()
	{
		for(int i=0;i<this->GetSize();i++)
			std::cout << *this->List[i] << ' ';
		std::cout << '\n';
	}
	int GetSize() const
    {
        return this->Size;
    }
	int GetCapacity() const
    {
        return this->Capacity;
    }

	ArrayIterator<T> GetBeginIterator()
	{
		ArrayIterator<T> tmp = {this->List[0],this->Size};
		return tmp;
	}
	ArrayIterator<T> GetEndIterator()
	{
		ArrayIterator<T> tmp = {this->List[this->Size-1], this->Size};
		return tmp;
	}

	ArrayIterator<T> begin()
    {
		return this->GetBeginIterator();
    }
    ArrayIterator<T> end()
    {
		return this->GetEndIterator();
    }

};