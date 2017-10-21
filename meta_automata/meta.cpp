#include <iostream>

template <bool N>
struct Val {
	static const bool value = N;
};

struct Nil {
	typedef Nil Head;
	typedef Nil Tail;
	static const int value = 0; // HACK
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
	static const int result = 1;
};

template <class B>
struct StateOut<Nil, B, Val<false> > {
	static const int result = 0;
};

template <class B>
struct StateOut<Nil, B, Val<true> > {
	static const int result = 1;
};

template <class A, class B>
struct StateOut<A, B, A> {
	static const int result = 0;
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

int main() {
	typedef List<Val<0>,
		List<Val<0>,
		List<Val<0>,
		List<Val<0>,
		List<Val<0>,
		List<Val<1>,
		List<Val<0>,
		List<Val<0>,
		List<Val<0>,
		List<Val<0>,
		List<Val<0>,
		Nil>>>>>>>>>>> testlist;

	typedef Step<testlist, Val<0> >::result next;
	std::cout << Get<next, 0 >::result::value;
	std::cout << Get<next, 1 >::result::value;
	std::cout << Get<next, 2 >::result::value;
	std::cout << Get<next, 3 >::result::value;
	std::cout << Get<next, 4 >::result::value;
	std::cout << Get<next, 5 >::result::value;
	std::cout << Get<next, 6 >::result::value;
	std::cout << Get<next, 7 >::result::value;
	std::cout << Get<next, 8 >::result::value;
	std::cout << Get<next, 9 >::result::value;
	std::cout << Get<next, 10 >::result::value << std::endl;

	return 0;
}
