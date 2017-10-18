data Tree a = Empty | Node (Tree a) a (Tree a)

find :: Ord a => Tree a -> a -> Bool
find Empty _ = False
find (Node lhs val rhs) needle
    | val == needle = True
    | val > needle = find lhs needle
    | val < needle = find rhs needle

insert :: Ord a => Tree a -> a -> Tree a
insert Empty item = (Node Empty item Empty)
insert (Node lhs val rhs) item
    | val == item = (Node lhs val rhs) -- Already in tree
    | val > item = (Node (insert lhs item) val rhs)
    | val < item = (Node lhs val (insert rhs item))

toList :: Ord a => Tree a -> [a]
toList Empty = []
toList (Node lhs val rhs) = (toList lhs) ++ [val] ++ (toList rhs)

toString :: Show a => Tree a -> [Char]
toString Empty = ""
toString (Node lhs val rhs) = "(" ++ toString lhs ++ " " ++ show val ++ " " ++ toString rhs ++ ")"
