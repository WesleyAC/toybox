#include <stdio.h>

typedef enum {
	NO = ' ',
	YES = '#',
	NEWLINE = '\n'
} val;

template <val N>
struct Val {
	static const val value = N;
};

struct Nil {
	typedef Nil Head;
	typedef Nil Tail;
	static const val value = NO; // HACK
};

template <typename H, typename T>
struct List {
	typedef H Head;
	typedef T Tail;
};

template <typename L, int N>
struct Get {
	typedef typename L::Tail Tail;
	typedef typename Get<Tail, N-1>::result result;
};

template <typename L>
struct Get<L, 0> {
	typedef typename L::Head result;
};

template <class A, class B, class C>
struct StateOut {
	static const val result = YES;
};

template <class B>
struct StateOut<Nil, B, Val<NO> > {
	static const val result = NO;
};

template <class B>
struct StateOut<Nil, B, Val<YES> > {
	static const val result = YES;
};

template <class A, class B>
struct StateOut<A, B, A> {
	static const val result = NO;
};

template <class L, class P>
struct Step {
	typedef typename L::Head CHead;
	typedef typename L::Tail CTail;

	typedef typename Step<CTail, CHead>::result Next;
	typedef List<Val<StateOut<Val<CTail::Head::value>, Val<CHead::value>, Val<P::value> >::result >, Next> result;
};

template <class P>
struct Step<Nil, P> {
	typedef Nil result;
};

template<unsigned N, class L>
struct PrintList {
	static void print() {
		printf("%c", Get<L, N-1>::result::value);
		PrintList<N-1, L>::print();
	}
};

template<class L>
struct PrintList<0, L> {
	static inline void print() {
		printf("\n");
	}
};


template<unsigned N, class L>
struct RunSim {
	static void run() {
		PrintList<11, L>::print();
		typedef typename Step<L, Val<NO> >::result next;
		RunSim<N-1, next>::run();
	}
};

template<class L>
struct RunSim<0, L> {
	static inline void run() {}
};

int main() {
	typedef List<Val<NO>, List<Val<NO>, List<Val<NO>, List<Val<NO>, List<Val<NO>, List<Val<YES>, List<Val<NO>, List<Val<NO>, List<Val<NO>, List<Val<NO>, List<Val<NO>, Nil>>>>>>>>>>> state;

	RunSim<7, state>::run();

	return 0;
}
