data Tree a = Empty | Node (Tree a) a (Tree a)

find :: Ord a => Tree a -> a -> Bool
find Empty _ = False
find (Node lhs val rhs) needle
	| val == needle = True
	| val > needle = find lhs needle
	| val < needle = find rhs needle
